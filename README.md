# 🎯 Portfólio - Gilberto Júnior

Um site de portfólio pessoal completo, desenvolvido com **Django** e **SQLite**, para showcasear seus projetos, habilidades e receber mensagens de contato.

---

## 📋 Características

✅ **Página Home** — Exibe resumo, projetos em destaque e habilidades  
✅ **Sobre Mim** — Biografia, foto de perfil, links de redes sociais e currículo  
✅ **Galeria de Projetos** — Filtrável por categoria com links para GitHub e demo  
✅ **Sistema de Contato** — Formulário para receber mensagens de visitantes  
✅ **Painel Admin** — Interface para gerenciar conteúdo do portfólio  
✅ **Design Responsivo** — CSS e JavaScript customizados para mobile/desktop  

---

## 🚀 Quick Start

### 1️⃣ Pré-requisitos
- Python 3.8+
- Git (opcional)

### 2️⃣ Setup Rápido

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python seed.py
python manage.py runserver
```

**Linux/Mac (Bash):**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python seed.py
python manage.py runserver
```

Ou execute o script de setup:
```bash
bash setup.sh
```

### 3️⃣ Acesse
- 🌐 **Site**: http://localhost:8000
- 🔐 **Admin**: http://localhost:8000/admin
- Login: `admin` / `admin123`

---

## 📁 Estrutura do Projeto

```
portfolio_gilberto/proj/
│
├── core/                    # App principal do Django
│   ├── models.py           # Modelos: Projeto, Habilidade, Contato, SobreMim
│   ├── views.py            # Lógica das páginas
│   ├── urls.py             # Rotas
│   ├── admin.py            # Configuração do painel admin
│   └── migrations/         # Histórico de mudanças no banco
│
├── portfolio_pkg/           # Configurações do projeto Django
│   ├── settings.py         # Configurações gerais
│   ├── urls.py             # URLs principais
│   └── wsgi.py             # Deploy
│
├── templates/               # Arquivos HTML
│   ├── base.html           # Template base
│   ├── home.html           # Página inicial
│   ├── sobre.html          # Sobre mim
│   ├── projetos.html       # Galeria de projetos
│   └── contato.html        # Formulário de contato
│
├── static/                  # Arquivos estáticos
│   ├── css/                # Estilos CSS
│   └── js/                 # Scripts JavaScript
│
├── db.sqlite3              # Banco de dados (será criado)
├── manage.py               # Gerenciador Django
├── requirements.txt        # Dependências Python
├── seed.py                 # Script para popular dados iniciais
└── README.md               # Este arquivo
```

---

## 🔧 Configuração

### Editar Informações Pessoais

1. Acesse http://localhost:8000/admin
2. Clique em **"Sobre Mim"** e edite seus dados:
   - Foto de perfil
   - Bio e descrição curta
   - Links: GitHub, LinkedIn, Email
   - Currículo em PDF
   - Localização

### Adicionar Projetos

No painel admin, clique em **"Projetos"** e crie novos com:
- Título e descrição
- Tecnologias utilizadas
- Links para GitHub e demo
- Imagem do projeto
- Categoria (Web, API, Bot, Dados, Outro)
- Destaque (apareça na home)

### Gerenciar Habilidades

Vá em **"Habilidades"** e configure:
- Nome (ex: Python, Django, React)
- Categoria (Linguagem, Framework, Banco de Dados, Ferramenta, Soft Skill)
- Nível de proficiência (0-100)
- Ícone (classe Font Awesome)

### Mensagens de Contato

Em **"Mensagens"**, visualize contatos recebidos e marque como lido.

---

## 📦 Dependências

```
Django >= 4.2
Pillow (para imagens)
```

Instale com: `pip install -r requirements.txt`

---

## 🎨 Customização

### Modificar Cores e Estilos
Edite os arquivos em `static/css/` conforme sua preferência de design.

### Adicionar Novas Páginas
1. Crie a função em `core/views.py`
2. Adicione a rota em `core/urls.py`
3. Crie o template em `templates/`

---

## 📤 Deploy

O projeto pode ser facilmente deployado em:
- **Heroku** — `python manage.py collectstatic`
- **PythonAnywhere**
- **AWS**, **DigitalOcean**, **Render**

> ⚠️ **Antes de fazer deploy:**
> - Mude `DEBUG = False` em `settings.py`
> - Gere uma nova `SECRET_KEY`
> - Configure as variáveis de ambiente

---

## 🛠️ Troubleshooting

### ❌ Porta 8000 já está em uso
```powershell
python manage.py runserver 8001
```

### ❌ Erro ao fazer upload de imagens
Certifique-se que a pasta `media/` existe e tem permissões de escrita.

### ❌ Banco de dados corrompido
```powershell
del db.sqlite3
python manage.py migrate
python seed.py
```

---

## 📞 Suporte

Dúvidas? Verifique:
- [Documentação Django](https://docs.djangoproject.com/)
- [Django Admin Customization](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)

---

## 📄 Licença

Projeto pessoal — Use livremente! 🚀

---

**Desenvolvido com ❤️ usando Django**
