from django.contrib import admin
from .models import Comment
from core.admin import ViewOnSiteMixin
# Register your models here.

@admin.register(Comment)
class CommentAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    list_display = ['id', '__str__', 'email', 'is_public', 'list_view_on_site']
    list_display_links = ['id', '__str__']
    readonly_fields = ('create_time',)
    search_fields = ['content', 'username']
    list_filter = ['create_time', 'is_public']

    fieldsets = (
        ('',{
           'fields':('username', 'email', 'website', 'ip_address'),
        }),
        ('comment', {
            'fields': ('content', 'is_public', 'create_time'),
        })
    )



