from core.models import AbstractCategory, AbstractTag, BaseBlogPost
from core.fields import MarkdownField




# Create your models here.
class NameSpaceMixin:
    name_space = 'code'


class Category(NameSpaceMixin, AbstractCategory):
    pass

class Tag(NameSpaceMixin, AbstractTag):
    pass

class BlogPost(NameSpaceMixin, BaseBlogPost):
    content = MarkdownField()
