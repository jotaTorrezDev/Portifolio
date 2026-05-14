from django.shortcuts import render, redirect
from django.contrib import messages
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
        if not all([nome,email,assunto,mensagem]):
            messages.error(request,'Preencha todos os campos.')
        else:
            Contato.objects.create(nome=nome,email=email,assunto=assunto,mensagem=mensagem)
            messages.success(request,'Mensagem enviada! Responderei em breve.')
            return redirect('contato')
    return render(request, 'contato.html', {'perfil':perfil})
