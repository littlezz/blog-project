__author__ = 'zz'
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.BlogListView.as_view(), name="blog_list_by_category"),
    url(r'^tag/(?P<tag>[\w-]+)/$', views.BlogListView.as_view(), name='blog_list_by_tag'),
    url(r'^$', views.BlogListView.as_view(), name='blog_list_all'),
    url(r'^(?P<slug>[\w-]+)/$', views.BlogDetailView.as_view(), name='blog_post_detail'),

]