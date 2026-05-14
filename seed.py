import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_pkg.settings')
django.setup()
from django.contrib.auth.models import User
from core.models import SobreMim, Projeto, Habilidade

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin','juniortorreszj@gmail.com','admin123')
    print("✓ Admin: admin / admin123")

if not SobreMim.objects.exists():
    SobreMim.objects.create(
        subtitulo='Desenvolvedor Python & Django',
        bio_curta='Fiscal em transição para a área de tecnologia. Apaixonado por Python, Django e desenvolvimento backend.',
        bio='Olá! Sou Gilberto Júnior, atualmente atuando como fiscal mas em plena transição para a área de desenvolvimento de software.\n\nVenho estudando programação de forma consistente, desenvolvendo projetos próprios para consolidar meu conhecimento em Python, Django, SQL, MySQL, HTML e CSS. Estou aprofundando meus estudos em APIs REST e desenvolvimento backend.\n\nSou focado, organizado e apaixonado por tecnologia. Busco constantemente evoluir e adquirir experiência prática para ingressar de vez na área de desenvolvimento.',
        github='https://github.com/jotaTorrezDev',
        linkedin='https://www.linkedin.com/in/gilberto-j%C3%BAnior-802b72270/',
        email='juniortorreszj@gmail.com',
        telefone='(21) 97702-3843',
        localizacao='Niterói, RJ',
    )
    print("✓ Perfil criado")

habs = [
    ('Python','linguagem',80,'bi-filetype-py',1),('HTML5','linguagem',85,'bi-filetype-html',2),('CSS3','linguagem',75,'bi-filetype-css',3),
    ('Django','framework',75,'bi-layers',1),('Bootstrap','framework',80,'bi-bootstrap',2),
    ('MySQL','banco',70,'bi-database',1),('SQLite','banco',75,'bi-database-fill',2),('SQL','banco',72,'bi-table',3),
    ('Git','ferramenta',75,'bi-git',1),('GitHub','ferramenta',80,'bi-github',2),('APIs REST','ferramenta',70,'bi-braces',3),
    ('Organização','soft',90,'bi-check2-circle',1),('Aprendizado contínuo','soft',95,'bi-book',2),
    ('Trabalho em equipe','soft',85,'bi-people',3),('Atenção aos detalhes','soft',90,'bi-eye',4),
]
for nome,cat,nivel,icone,ordem in habs:
    Habilidade.objects.get_or_create(nome=nome, defaults=dict(categoria=cat,nivel=nivel,icone=icone,ordem=ordem))
print(f"✓ {len(habs)} habilidades criadas")

projs = [
    dict(titulo='QRHub — Gerador de QR Code',descricao='Sistema web para lançar qualquer quantidade de códigos e gerar um único QR Code. Inclui login, cadastro, painel admin, histórico e download PNG.',tecnologias='Python, Django, SQLite, Bootstrap',url_github='https://github.com/jotaTorrezDev',categoria='web',destaque=True,ordem=1),
    dict(titulo='Controle de Estoque com QR Code',descricao='Aplicação de controle de estoque com sistema de cargos, geração de QR Code para produtos, dashboard interativo e gestão de usuários.',tecnologias='Python, Django, SQLite, Bootstrap',url_github='https://github.com/jotaTorrezDev',categoria='web',destaque=True,ordem=2),
    dict(titulo='API REST com Django',descricao='Projeto de estudo de APIs RESTful usando Django, com autenticação, endpoints CRUD e integração com banco de dados.',tecnologias='Python, Django, MySQL, REST',url_github='https://github.com/jotaTorrezDev',categoria='api',destaque=True,ordem=3),
]
for p in projs:
    Projeto.objects.get_or_create(titulo=p['titulo'], defaults=p)
print(f"✓ {len(projs)} projetos criados")
print("\n✅ Pronto! Acesse: http://localhost:8000")
print("   Admin:  http://localhost:8000/admin  |  admin / admin123")
