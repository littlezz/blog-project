from django.db import models
from django.core.urlresolvers import reverse
from core.models import AbstractCategory, AbstractTag, BaseBlogPost
from core.fields import MarkdownField




# Create your models here.


class Category(AbstractCategory):
    pass

class Tag(AbstractTag):
    pass


class BlogPost(BaseBlogPost):
    content = MarkdownField()

