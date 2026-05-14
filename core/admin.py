from django.contrib import admin
from .models import Projeto, Habilidade, Contato, SobreMim

@admin.register(SobreMim)
class SobreMimAdmin(admin.ModelAdmin):
    list_display = ['subtitulo','email','localizacao','ativo']

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display=['titulo','categoria','destaque','ordem']
    list_editable=['destaque','ordem']; list_filter=['categoria','destaque']; search_fields=['titulo','descricao']

@admin.register(Habilidade)
class HabilidadeAdmin(admin.ModelAdmin):
    list_display=['nome','categoria','nivel','ordem']; list_editable=['nivel','ordem']; list_filter=['categoria']

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display=['nome','email','assunto','lido','enviado_em']; list_editable=['lido']
    readonly_fields=['nome','email','assunto','mensagem','enviado_em']
