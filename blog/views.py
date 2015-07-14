from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import BlogPost, Category
from core.views import BaseBlogDetailView, BaseBlogListView, BaseGetContextMixin, BaseMonthArchive, BaseYearArchive


class GetContextMixin(BaseGetContextMixin):
    category = Category


class BlogListView(GetContextMixin, BaseBlogListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'





class BlogDetailView(GetContextMixin, BaseBlogDetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'


class YearArchiveView(GetContextMixin, BaseYearArchive):
    model = BlogPost


class MonthArchiveView(GetContextMixin, BaseMonthArchive):
    model =  BlogPost