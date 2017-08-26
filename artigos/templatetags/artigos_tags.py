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


@register.simple_tag(takes_context=True)
def lista_de_marcações(context, tipo='c', separador=' '):
    """Obtém a lista de categorias ou etiquetas de um artigo."""
    html = '<i class="fa fa-archive"></i>' if tipo == 'c' else '<i class="fa fa-tags"></i>'
    html += ' <a>{}</a>'

    def obter_link(objeto):
        """Obtém o link para esse objeto."""
        return html.format(objeto.nome)

    artigo = context['artigo']
    objetos = artigo.categorias.all() if tipo == 'c' else artigo.etiquetas.all()
    return safestring.mark_safe(separador.join(map(obter_link, objetos)))
