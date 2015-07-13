from core.models import AbstractCategory, AbstractTag, BaseBlogPost
from core.fields import MarkdownField
from core.utils import markdown_render
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment


# Create your models here.
class NameSpaceMixin:
    name_space = 'code'


class Category(NameSpaceMixin, AbstractCategory):
    pass

class Tag(NameSpaceMixin, AbstractTag):
    pass


class BlogPost(NameSpaceMixin, BaseBlogPost):
    content = MarkdownField()
    comments = GenericRelation(Comment)

    class Meta(BaseBlogPost.Meta):
        verbose_name = 'post of code'

    def rendered_content(self):
        return markdown_render(self.content)
