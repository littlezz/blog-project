from django.contrib import admin
from . import models
# Register your models here.
from core.admin import PostAdmin, SlugAdmin


@admin.register(models.BlogPost)
class BlogPostAdmin(PostAdmin):
    pass


admin.site.register((models.Tag, models.Category), SlugAdmin)