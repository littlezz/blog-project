from core.models import AbstractCategory, AbstractTag, BaseBlogPost
from core.fields import MarkdownField
from core.utils import markdown_render



# Create your models here.
class NameSpaceMixin:
    name_space = 'code'


class Category(NameSpaceMixin, AbstractCategory):
    pass

class Tag(NameSpaceMixin, AbstractTag):
    pass


class BlogPost(NameSpaceMixin, BaseBlogPost):
    content = MarkdownField()

    def rendered_content(self):
        return markdown_render(self.content)