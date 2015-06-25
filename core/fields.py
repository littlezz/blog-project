from django.db.models import TextField
from markdown2 import markdown
from django_markdown.widgets import MarkdownWidget
from ckeditor.widgets import CKEditorWidget
# from tinymce.widgets import AdminTinyMCE
from redactor.widgets import RedactorEditor
__author__ = 'zz'


class MarkdownField(TextField):

    def formfield(self, **kwargs):
        kwargs['widget'] = MarkdownWidget
        return super().formfield(**kwargs)


class RichTextField(TextField):
    def formfield(self, **kwargs):
        kwargs['widget'] = RedactorEditor
        return super().formfield(**kwargs)
