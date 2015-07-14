from .models import BlogPost, Category
from core.views import BaseBlogDetailView, BaseBlogListView, BaseGetContextMixin, BaseYearArchive, BaseMonthArchive



class GetContextMixin(BaseGetContextMixin):
    category = Category


class BlogListView(GetContextMixin, BaseBlogListView):
    model = BlogPost
    template_name = 'code_post/blog_list.html'





class BlogDetailView(GetContextMixin, BaseBlogDetailView):
    model = BlogPost
    template_name = 'code_post/blog_detail.html'


class YearArchiveView(GetContextMixin, BaseYearArchive):
    model = BlogPost


class MonthArchiveView(GetContextMixin, BaseMonthArchive):
    model = BlogPost