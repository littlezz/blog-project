from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from core.fields import MarkdownField
from django.contrib.auth.models import Permission
from core.models import TimeStamp
from .managers import CommentManager
# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        abstract = True




class Comment(TimeStamp, UserInfo):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    content = MarkdownField()
    is_public = models.BooleanField(default=True)

    objects = CommentManager()


    def __str__(self):
        return '{}: {}'.format(self.username, self.content)

    def get_absolute_url(self):
        return self.content_object.get_absolute_url + '#comment{}'.format(self.id)
