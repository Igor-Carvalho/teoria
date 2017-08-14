"""Tags e filtros da aplicação artigos."""

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def obter_caminho_da_imagem(context, nome_da_imagem):
    """Obtém o caminho de uma imagem de artigo utilizando seu nome."""
    return context['artigo'].imagens.get(nome=nome_da_imagem).caminho.url
