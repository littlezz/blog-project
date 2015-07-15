from django.conf.urls import include, url
from . import views
from core.urls import generate_core_urls


urlpatterns = generate_core_urls(views)
