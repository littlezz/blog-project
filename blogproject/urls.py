"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog import urls as blog_urls
from django.views.generic import TemplateView
from gallry import urls as gallry_urls
from django.conf import settings
from django.conf.urls.static import static
from code_post import urls as code_urls

urlpatterns = [
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog_urls, namespace='blog')),
    url(r'^code/', include(code_urls, namespace='code')),
    url(r'^$', TemplateView.as_view(template_name='welcome.html')),
    url(r'^images/', include(gallry_urls)),
    # url(r'^ckeditor/', include('ckeditor.urls')),
    # url(r'^tinymce/', include('tinymce.urls')),
    url(r'^redactor/', include('redactor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

