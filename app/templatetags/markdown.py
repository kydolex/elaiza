from django import template
from django.template.defaultfilters import stringfilter
from markdownx.settings import (
    MARKDOWNX_MARKDOWN_EXTENSIONS,
    MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS
)
import markdown as md
 
register = template.Library()
 
@register.filter()
@stringfilter

def markdown(value):
    return md.markdown(value, extensions=[
        'markdown.extensions.extra',  
        'markdown.extensions.abbr',
        'markdown.extensions.attr_list',
        'markdown.extensions.def_list',
        'markdown.extensions.fenced_code',
        'markdown.extensions.footnotes',
        'markdown.extensions.md_in_html',
        'markdown.extensions.tables',

        'markdown.extensions.admonition',
        'markdown.extensions.codehilite',
        'markdown.extensions.legacy_attrs',
        'markdown.extensions.legacy_em',
        'markdown.extensions.meta',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
        'markdown.extensions.smarty',
        'markdown.extensions.toc',
        'markdown.extensions.wikilinks',

        
        'extra', 
        'abbr', 
        'attr_list',
        'def_list',
        'fenced_code',
        'footnotes',
        'md_in_html',
        'tables',
        'admonition',
        'codehilite',
        'legacy_attrs',
        'legacy_em',
        'meta',
        'nl2br',
        'sane_lists',
        'smarty',
        'toc',
        'wikilinks'
        ])

def markdownify(content):
    """
    ...
    """
    # Python-Markdownライブラリ
    md = markdown(
        text=content,
        extensions=MARKDOWNX_MARKDOWN_EXTENSIONS,
        extension_configs=MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS
    )
    return md