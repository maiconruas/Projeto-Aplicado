from django.contrib import admin
from funko.forms import VariacaoObrigatoria
from post import models


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    formset = VariacaoObrigatoria
    min_num = 1
    extra = 0
    can_delete = True


class PostAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta']
    inlines = [
        VariacaoInline
    ]


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Variacao)
