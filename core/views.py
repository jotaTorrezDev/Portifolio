import json
import logging
import urllib.error
import urllib.request

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Projeto, Habilidade, Contato, SobreMim

logger = logging.getLogger(__name__)


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


def enviar_email_resend(assunto, nome, email, mensagem):
    payload = {
        'from': settings.DEFAULT_FROM_EMAIL,
        'to': [settings.CONTACT_EMAIL],
        'subject': f'[Contato do portfólio] {assunto}',
        'text': f'Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}',
        'reply_to': email,
    }
    req = urllib.request.Request(
        'https://api.resend.com/emails',
        data=json.dumps(payload).encode('utf-8'),
        headers={
            'Authorization': f'Bearer {settings.RESEND_API_KEY}',
            'Content-Type': 'application/json',
            'User-Agent': 'portfolio-django/1.0',
        },
        method='POST',
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.status


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
                enviar_email_resend(assunto, nome, email, mensagem)
            except urllib.error.HTTPError as e:
                logger.error('Resend respondeu %s: %s', e.code, e.read().decode('utf-8', 'ignore'))
                messages.error(request,'Não foi possível enviar a mensagem. Tente novamente mais tarde.')
            except Exception:
                logger.exception('Erro ao enviar email de contato')
                messages.error(request,'Não foi possível enviar a mensagem. Tente novamente mais tarde.')
            else:
                messages.success(request,'Mensagem enviada! Responderei em breve.')
                return redirect('contato')
    return render(request, 'contato.html', {'perfil': perfil})
