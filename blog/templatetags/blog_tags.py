from django.template import Library
from markdown2 import markdown
from bleach import clean
from core import default_settings as settings
__author__ = 'zz'

register = Library()



HTML_ClASSES = {
        'img': 'img-responsive center-block',
}

@register.filter
def markdown_render(value):
    extras = {
            'fenced-code-blocks': True,
            'html-classes': HTML_ClASSES,
    }
    return clean(markdown(value, extras=extras),
                 tags=settings.ALLOW_TAGS, attributes=settings.ALLOW_ATTRS, styles=settings.ALLOW_STYLES)


