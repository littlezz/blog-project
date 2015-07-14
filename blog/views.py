from .models import BlogPost
from core.views import BaseBlogDetailView, BaseBlogListView, BaseMonthArchive, BaseYearArchive




class BlogListView(BaseBlogListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'




class BlogDetailView(BaseBlogDetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'


class YearArchiveView(BaseYearArchive):
    model = BlogPost


class MonthArchiveView(BaseMonthArchive):
    model =  BlogPost