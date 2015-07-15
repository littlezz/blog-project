from django.core.urlresolvers import reverse
from django.template import Library, defaulttags
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


@register.simple_tag(takes_context=True)
def simple_url(context, obj, *args, **kwargs):
    """
    :param obj:  the url name same as the {% url %}
    :return: if the is no ':' in the viewname, the function will add the current_ns from the context.
    """
    ns = context.get('current_ns')

    if ns and (':' not in obj):
        obj = ':'.join((ns, obj))

    return reverse(obj, args=args, kwargs=kwargs)


@register.inclusion_tag('includes/month_links_snippet.html', takes_context=True)
def month_links(context):
    model = context.get('model')
    if not model:
        return None

    context.update({
        'dates': model.objects.publish().datetimes('publish_date', 'month')

    })
    return context