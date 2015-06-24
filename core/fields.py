from django.db.models import TextField
from markdown2 import markdown
from django_markdown.widgets import MarkdownWidget
__author__ = 'zz'


class MarkdownField(TextField):

    def formfield(self, **kwargs):
        kwargs['widget'] = MarkdownWidget
        return super().formfield(**kwargs)