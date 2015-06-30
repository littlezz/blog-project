__author__ = 'zz'
from markdown2 import markdown
from bleach import clean
from core import default_settings as settings



def markdown_render(value):
    extras = (
            'fenced-code-blocks',
    )
    return clean(markdown(value, extras=extras),
                 tags=settings.ALLOW_TAGS, attributes=settings.ALLOW_ATTRS, styles=settings.ALLOW_STYLES)


