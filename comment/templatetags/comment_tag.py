from django.template import Library
from comment.forms import CommentForm

__author__ = 'zz'

register = Library()

@register.inclusion_tag('includes/list_comments.html', takes_context=True)
def list_comments(context, obj):
    queryset = obj.comments.visible()
    count = len(queryset)
    return {
        'comments': queryset,
        'comments_count': count,
    }

@register.inclusion_tag('includes/comment_form.html', takes_context=True)
def comment_form_for(context, obj):
    form = CommentForm(obj)
    return {
        'form': form
    }