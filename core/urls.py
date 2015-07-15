from django.conf.urls import url
__author__ = 'zz'


def generate_core_urls(views):
    urlpatterns = [
        url(r'^category/(?P<category_slug>[\w-]+)/$', views.BlogListView.as_view(), name="blog_list_by_category"),
        url(r'^tag/(?P<tag>[\w-]+)/$', views.BlogListView.as_view(), name='blog_list_by_tag'),
        url(r'^$', views.BlogListView.as_view(), name='blog_list_all'),
        url(r'^(?P<year>[0-9]{4})/$', views.YearArchiveView.as_view(), name='year_archive'),
        url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$', views.MonthArchiveView.as_view(), name='month_archive'),
        url(r'^(?P<slug>[\w-]+)/$', views.BlogDetailView.as_view(), name='blog_post_detail'),

    ]
    return urlpatterns
