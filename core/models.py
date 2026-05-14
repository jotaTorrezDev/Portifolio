from django.db import models

class Projeto(models.Model):
    CATEGORIAS = [('web','Web'),('api','API / Backend'),('bot','Bot / Automação'),('dados','Dados'),('outro','Outro')]
    titulo       = models.CharField(max_length=120)
    descricao    = models.TextField()
    tecnologias  = models.CharField(max_length=200, help_text='ex: Python, Django, MySQL')
    url_github   = models.URLField(blank=True, verbose_name='Link GitHub')
    url_demo     = models.URLField(blank=True, verbose_name='Link Demo')
    imagem       = models.ImageField(upload_to='projetos/', blank=True, null=True)
    categoria    = models.CharField(max_length=20, choices=CATEGORIAS, default='web')
    destaque     = models.BooleanField(default=False)
    ordem        = models.PositiveIntegerField(default=0)
    criado_em    = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['ordem','-criado_em']
        verbose_name='Projeto'; verbose_name_plural='Projetos'
    def __str__(self): return self.titulo
    def tecnologias_lista(self): return [t.strip() for t in self.tecnologias.split(',')]

class Habilidade(models.Model):
    CATEGORIAS = [('linguagem','Linguagem'),('framework','Framework'),('banco','Banco de Dados'),('ferramenta','Ferramenta'),('soft','Soft Skill')]
    nome      = models.CharField(max_length=60)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='linguagem')
    nivel     = models.PositiveIntegerField(default=80)
    icone     = models.CharField(max_length=60, blank=True)
    ordem     = models.PositiveIntegerField(default=0)
    class Meta:
        ordering=['categoria','ordem']; verbose_name='Habilidade'; verbose_name_plural='Habilidades'
    def __str__(self): return self.nome

class Contato(models.Model):
    nome=models.CharField(max_length=100); email=models.EmailField()
    assunto=models.CharField(max_length=150); mensagem=models.TextField()
    lido=models.BooleanField(default=False); enviado_em=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-enviado_em']; verbose_name='Mensagem'; verbose_name_plural='Mensagens'
    def __str__(self): return f'{self.nome} — {self.assunto}'

class SobreMim(models.Model):
    subtitulo     = models.CharField(max_length=200, default='Desenvolvedor Python & Django')
    bio           = models.TextField()
    bio_curta     = models.CharField(max_length=300)
    foto          = models.ImageField(upload_to='perfil/', blank=True, null=True)
    github        = models.URLField(blank=True)
    linkedin      = models.URLField(blank=True)
    email         = models.EmailField(blank=True)
    telefone      = models.CharField(max_length=20, blank=True)
    localizacao   = models.CharField(max_length=100, blank=True, default='Niterói, RJ')
    curriculo_pdf = models.FileField(upload_to='docs/', blank=True, null=True)
    ativo         = models.BooleanField(default=True)
    class Meta:
        verbose_name='Sobre Mim'; verbose_name_plural='Sobre Mim'
    def __str__(self): return self.subtitulo
