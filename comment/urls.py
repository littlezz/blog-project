from django.conf.urls import url
from . import views
__author__ = 'zz'


urlpatterns = [
    url('^comment/$', views.CommentView.as_view(), name='comment-post'),
]
