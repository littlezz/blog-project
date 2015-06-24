from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost, Category
# Create your views here.

class GetContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(specie=self.kwargs['specie'])
        context['specie'] = self.kwargs['specie']
        return context


class BlogListView(GetContextMixin, ListView):
    context_object_name = 'blog_list'
    template_name = 'blog/blog_list.html'
    paginate_by = 5

    def get_queryset(self):
        specie = self.kwargs['specie']
        category_slug =  self.kwargs.get('category_slug')
        tag = self.kwargs.get('tag')

        queryset = BlogPost.objects.publish().filter(specie=specie)

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        if tag:
            queryset = queryset.filter(tags__slug=tag)

        print(queryset)
        return queryset




class BlogDetailView(GetContextMixin, DetailView):
    queryset = BlogPost.objects.publish()
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

