from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView, MonthArchiveView


class BaseGetContextMixin:
    category = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.category.objects.all()
        context['category'] = self.kwargs.get('category_slug')
        context['tag'] = self.kwargs.get('tag')
        return context

class GetQuerysetMixin:
    def get_queryset(self):
        if not self.model:
            raise NotImplemented('Must set model')

        category_slug =  self.kwargs.get('category_slug')
        tag = self.kwargs.get('tag')

        queryset = self.model.objects.publish()

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        if tag:
            queryset = queryset.filter(tags__slug=tag)

        return queryset



class BaseBlogListView(GetQuerysetMixin, ListView):
    context_object_name = 'blog_list'
    paginate_by = 5




class BaseBlogDetailView(GetQuerysetMixin, DetailView):
    context_object_name = 'blog'



class _ArchiveMixin:
    context_object_name = 'blog_list'
    date_field = 'publish_date'
    template_name_suffix = ''

    def get_template_names(self):
        return '{}/blog_list.html'.format(self.model._meta.app_label)



class BaseYearArchive(_ArchiveMixin, YearArchiveView):
    make_object_list = True


class BaseMonthArchive(_ArchiveMixin, MonthArchiveView):
    month_format='%m'

