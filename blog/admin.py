from django.contrib import admin
from . import models
from core.admin import PostAdmin, SlugAdmin
# Register your models here.


@admin.register(models.BlogPost)
class BlogPostAdmin(PostAdmin):
    pass


admin.site.register((models.Tag, models.Category), SlugAdmin)