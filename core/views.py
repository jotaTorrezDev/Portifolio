from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Projeto, Habilidade, Contato, SobreMim

def get_perfil():
    return SobreMim.objects.filter(ativo=True).first()

def home(request):
    perfil = get_perfil()
    projetos = Projeto.objects.filter(destaque=True)[:4]
    habilidades = {k: Habilidade.objects.filter(categoria=k) for k in ('linguagem','framework','banco','ferramenta','soft')}
    return render(request, 'home.html', {'perfil':perfil,'projetos':projetos,'habilidades':habilidades})

def sobre(request):
    perfil = get_perfil()
    habilidades = Habilidade.objects.all()
    return render(request, 'sobre.html', {'perfil':perfil,'habilidades':habilidades})

def projetos(request):
    perfil = get_perfil()
    categoria = request.GET.get('cat','')
    todos = Projeto.objects.filter(categoria=categoria) if categoria else Projeto.objects.all()
    return render(request, 'projetos.html', {'perfil':perfil,'projetos':todos,'cats':Projeto.CATEGORIAS,'cat_ativa':categoria})

def contato(request):
    perfil = get_perfil()
    if request.method == 'POST':
        nome=request.POST.get('nome','').strip(); email=request.POST.get('email','').strip()
        assunto=request.POST.get('assunto','').strip(); mensagem=request.POST.get('mensagem','').strip()
        try:
            validate_email(email)
        except ValidationError:
            email_valido = False
        else:
            email_valido = True

        if not all([nome,email,assunto,mensagem]) or not email_valido:
            messages.error(request,'Preencha todos os campos.')
        else:
            Contato.objects.create(nome=nome,email=email,assunto=assunto,mensagem=mensagem)
        try:
            email_msg = EmailMessage(
                subject=f'[Contato do portfólio] {assunto}',
                body=(
                    f'Nome: {nome}\n'
                    f'Email: {email}\n\n'
                    f'Mensagem:\n{mensagem}'
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email],
            )
            email_msg.send(fail_silently=False)
        except Exception as e:
            print(f"ERRO AO ENVIAR EMAIL: {e}")
            messages.error(request,'Não foi possível enviar a mensagem. Tente novamente mais tarde.')
        else:
            messages.success(request,'Mensagem enviada! Responderei em breve.')
            return redirect('contato')
