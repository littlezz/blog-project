from django.db import models
from django.core.urlresolvers import reverse
from core.models import AbstractCategory, AbstractTag, BaseBlogPost
from core.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment



# Create your models here.
class NameSpaceMixin:
    name_space = 'blog'


class Category(NameSpaceMixin, AbstractCategory):
    pass


class Tag(NameSpaceMixin, AbstractTag):
    pass


class BlogPost(NameSpaceMixin, BaseBlogPost):
    content = RichTextField()
    comments = GenericRelation(Comment)

    class Meta(BaseBlogPost.Meta):
        verbose_name = 'post of blog'
