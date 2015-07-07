from django.db.models import Manager
__author__ = 'zz'

class CommentManager(Manager):

    def visible(self):
        return self.filter(is_public=True)
