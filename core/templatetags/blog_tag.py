from django.template import Library
__author__ = 'zz'

register = Library()


@register.inclusion_tag('includes/render_next_or_previous_blog.html', takes_context=True)
def next_or_previous_blog(context, obj):
    has_previous = False
    has_next = False

    next_blog = obj.get_next_object()
    previous_blog = obj.get_previous_object()

    if next_blog:
        has_next = True

    if previous_blog:
        has_previous = True

    return {
        'next_blog': next_blog,
        'previous_blog': previous_blog,
        'has_next': has_next,
        'has_previous': has_previous
    }