"""Tags e filtros da aplicação artigos."""

from django import template
from django.utils import safestring, text

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
                 <img src="{caminho_da_imagem}" style="{style}" class="post-imagem" />
               </a>'''

    return safestring.mark_safe(html)


@register.simple_tag(takes_context=True)
def renderizar_conteúdo_do_artigo(context, truncate=None):
    """Renderiza o conteúdo do artigo novamente para processar tags e filtros presentes."""
    conteúdo = template.Template(context['artigo'].conteúdo).render(context=context)
    if truncate is None:
        return conteúdo

    conteúdo = text.Truncator(conteúdo).words(int(truncate), html=True)
    return safestring.mark_safe(conteúdo)


@register.filter
def query_join(queryset, char=' &#x7C; '):
    """Como join, mas para um queryset."""
    return safestring.mark_safe(char.join(map(str, queryset)))
