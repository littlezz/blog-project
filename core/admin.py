from django.contrib import admin

# Register your models here.

class ViewOnSiteMixin:
    def view_on_site(self, obj):
        return '<a href="{}">View on site</a>'.format(obj.get_absolute_url())

    view_on_site.allow_tags = True


class PostAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    list_display = ['title', 'publish_date', 'update_time', 'category','description', 'view_on_site']
    readonly_fields = ['update_time', 'create_time']
    exclude = ['auto_description']
    search_fields = ['title', 'content', 'id', 'update_time']
    list_filter = ['update_time', 'publish_date']


class SlugAdmin(admin.ModelAdmin):
    pass