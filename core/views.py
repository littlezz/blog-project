from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView


class BaseGetContextMixin:
    category = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.category.objects.all()
        return context


class BaseBlogListView(ListView):
    context_object_name = 'blog_list'
    paginate_by = 5

    def get_queryset(self):
        category_slug =  self.kwargs.get('category_slug')
        tag = self.kwargs.get('tag')

        queryset = self.queryset

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        if tag:
            queryset = queryset.filter(tags__slug=tag)

        print(queryset)
        return queryset




class BaseBlogDetailView(DetailView):
    context_object_name = 'blog'