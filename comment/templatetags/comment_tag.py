from django.template import Library
__author__ = 'zz'

register = Library()

@register.inclusion_tag('includes/list_comments.html', takes_context=True)
def list_comments(context, obj):
    pass