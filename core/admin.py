from django.contrib import admin

# Register your models here.

class ViewOnSiteMixin:
    def list_view_on_site(self, obj):
        return '<a href="{}">View on site</a>'.format(obj.get_absolute_url())

    list_view_on_site.allow_tags = True


class PostAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'publish_date', 'update_time', 'category', 'list_view_on_site']
    readonly_fields = ['update_time', 'create_time']
    exclude = ['auto_description']
    search_fields = ['title', 'content', 'id', 'update_time']
    list_filter = ['update_time', 'publish_date']

    fieldsets = (
        ('', {
            'fields': ('title', 'category', 'feature_image', 'content', 'tags')
        }),
        ('Others', {
            'classes': ('grp-collapse grp-closed',),
            'fields':('custom_description', 'slug', 'publish_date', 'expire_date'),
        }),
        ('Info', {
            'classes': ('grp-collapse grp-open',),
            'fields': ('create_time', 'update_time')
        })
    )

    raw_id_fields = ['tags']
    autocomplete_lookup_fields = {
        'm2m': ['tags'],
    }


class SlugAdmin(admin.ModelAdmin):
    pass