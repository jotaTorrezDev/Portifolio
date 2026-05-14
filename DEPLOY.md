# 🚀 GUIA DE DEPLOY

Seu projeto **está 90% pronto** para produção. Siga este guia para torná-lo 100% seguro!

---

## 📋 Checklist Pré-Deploy

- [ ] Instalar `python-decouple`: `pip install python-decouple`
- [ ] Gerar `SECRET_KEY` forte
- [ ] Criar arquivo `.env` na raiz do projeto
- [ ] Configurar `ALLOWED_HOSTS` com seu domínio
- [ ] Executar `python manage.py collectstatic`
- [ ] Testar com `DEBUG=False` localmente
- [ ] Fazer backup do banco de dados

---

## 🔐 Passo 1: Gerar SECRET_KEY Forte

No PowerShell:
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copie a saída e use no `.env`.

---

## 📁 Passo 2: Criar Arquivo `.env`

Crie um arquivo `.env` **na raiz do projeto** (mesma pasta de `manage.py`):

```env
SECRET_KEY=sua-chave-aleatoria-gerada-acima
DEBUG=False
ALLOWED_HOSTS=meu-portfolio.com,www.meu-portfolio.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

> ⚠️ **IMPORTANTE:** Nunca faça commit do `.env`! Já está no `.gitignore`

---

## 🧪 Passo 3: Testar Localmente em Modo Produção

```powershell
# Ativar ambiente virtual
.venv\Scripts\Activate.ps1

# Instalar dependência
pip install python-decouple

# Recolher arquivos estáticos
python manage.py collectstatic --noinput

# Rodar servidor com DEBUG=False
python manage.py runserver --settings=portfolio_pkg.settings_production
```

Se tudo funcionar, está pronto para deploy!

---

## 🌍 Passo 4: Escolha Sua Plataforma de Deploy

### ✅ **OPÇÃO 1: Heroku (Mais Fácil)**

1. Instale Heroku CLI
2. Faça login: `heroku login`
3. Crie app: `heroku create meu-portfolio`
4. Configure variáveis:
   ```powershell
   heroku config:set SECRET_KEY=sua-chave
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=meu-portfolio.herokuapp.com
   heroku config:set SECURE_SSL_REDIRECT=True
   ```
5. Faça deploy:
   ```powershell
   git push heroku main
   ```

---

### ✅ **OPÇÃO 2: PythonAnywhere (Recomendado para iniciantes)**

1. Acesse: https://www.pythonanywhere.com
2. Crie conta grátis
3. Upload seu código via Git ou ZIP
4. Configure Web app com Django
5. Edite arquivo de configuração (`/var/www/seu_usuario_pythonanywhere_com_wsgi.py`)

---

### ✅ **OPÇÃO 3: Render (Gratuito + Moderno)**

1. Acesse: https://render.com
2. Conecte seu repositório GitHub
3. Crie novo Web Service
4. Configure variáveis de ambiente no painel
5. Deploy automático a cada push!

---

### ✅ **OPÇÃO 4: DigitalOcean (Melhor Performance)**

1. Crie Droplet com Ubuntu 22.04
2. SSH no servidor
3. Clone seu repositório
4. Configure Nginx + Gunicorn + Supervisor
5. Aponte domínio para IP do Droplet

**Script de setup (Linux):**
```bash
# Update
sudo apt update && sudo apt upgrade -y

# Dependências
sudo apt install python3-pip python3-venv nginx -y

# Clone projeto
git clone seu-repositorio /var/www/portfolio
cd /var/www/portfolio

# Virtual env
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Coletar estáticos
python manage.py collectstatic --noinput

# Instalar Gunicorn
pip install gunicorn

# Testar Gunicorn
gunicorn portfolio_pkg.wsgi --bind 0.0.0.0:8000

# Configurar Supervisor (auto-restart)
sudo nano /etc/supervisor/conf.d/portfolio.conf
```

---

## 📊 Dados no Banco em Produção

Se estiver usando SQLite (não recomendado para múltiplos usuários):
- ✅ Funciona bem para portfólio pessoal
- ❌ Não escala para muitos acessos simultâneos

Para crescer, use **PostgreSQL**:
```powershell
# Instalar driver
pip install psycopg2-binary

# Atualizar settings para usar PostgreSQL
# DATABASE_URL=postgresql://user:password@localhost:5432/portfolio_db
```

---

## 🔄 Deploy Contínuo (CI/CD)

### GitHub Actions (Automático a cada push)

Crie `.github/workflows/deploy.yml`:

```yaml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Run deploy script
      run: |
        echo "Executando testes e deploy..."
        python manage.py test
        # Seu comando de deploy aqui
```

---

## ✅ Checklist Final de Segurança

- [ ] `DEBUG = False`
- [ ] `SECRET_KEY` aleatória
- [ ] `ALLOWED_HOSTS` específicos (não `*`)
- [ ] SSL/HTTPS ativado
- [ ] Cookies seguros configurados
- [ ] `.env` no `.gitignore`
- [ ] Banco de dados seguro (backup regular)
- [ ] Permissões de arquivo corretas (755 para dirs, 644 para files)
- [ ] Logs configurados
- [ ] Email de contato funcionando

---

## 🆘 Troubleshooting

### ❌ "Static files not found in production"
```powershell
python manage.py collectstatic --clear --noinput
```

### ❌ "DisallowedHost error"
Verifique `ALLOWED_HOSTS` no `.env` para incluir seu domínio.

### ❌ "CSRF token missing"
Configure `CSRF_COOKIE_SECURE = True` e use HTTPS.

### ❌ "Database locked (SQLite)"
Use PostgreSQL em produção com múltiplos workers.

---

## 📞 Próximos Passos

1. ✅ Escolher plataforma (Heroku/PythonAnywhere/Render/DigitalOcean)
2. ✅ Configurar domínio personalizado
3. ✅ Ativar SSL/HTTPS
4. ✅ Configurar backups automáticos
5. ✅ Monitorar performance e logs

---

**Sucesso no deploy! 🎉**
