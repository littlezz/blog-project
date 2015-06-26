from django.db.models import TextField
from django_markdown.widgets import MarkdownWidget
from redactor.widgets import RedactorEditor
from core import default_settings as settings
from bleach import clean

__author__ = 'zz'


class MarkdownField(TextField):

    def formfield(self, **kwargs):
        kwargs['widget'] = MarkdownWidget
        return super().formfield(**kwargs)


class RichTextField(TextField):
    def formfield(self, **kwargs):
        kwargs['widget'] = RedactorEditor
        return super().formfield(**kwargs)

    def to_python(self, value):
        return clean(value,
                     tags=settings.ALLOW_TAGS,
                     attributes=settings.ALLOW_ATTRS,
                     styles=settings.ALLOW_STYLES
                     )

