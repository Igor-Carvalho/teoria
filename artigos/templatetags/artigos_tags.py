"""Tags e filtros da aplicação artigos."""

from django import template
from django.utils import safestring

register = template.Library()


@register.simple_tag(takes_context=True)
def obter_caminho_da_imagem(context, nome_da_imagem):
    """Obtém o caminho de uma imagem de artigo utilizando seu nome."""
    return context['artigo'].imagens.get(nome=nome_da_imagem).caminho.url


@register.simple_tag(takes_context=True)
def fancy_box(context, nome_da_imagem, group='', style=''):
    """Renderiza o markup mínimo necessário para uma fancybox."""
    caminho_da_imagem = obter_caminho_da_imagem(context, nome_da_imagem)
    html = f'''<a data-fancybox="{group}" href="{caminho_da_imagem}">
                 <img src="{caminho_da_imagem}" style="{style}" />
               </a>'''
    return safestring.mark_safe(html)
