
__author__ = 'zz'

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.GallryListView.as_view(), name='image_list'),
    url(r'^upload/$', views.UploadImageView.as_view()),
]
