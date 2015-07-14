from .models import BlogPost
from core.views import BaseBlogDetailView, BaseBlogListView, BaseYearArchive, BaseMonthArchive



class BlogListView(BaseBlogListView):
    model = BlogPost
    template_name = 'code_post/blog_list.html'



class BlogDetailView(BaseBlogDetailView):
    model = BlogPost
    template_name = 'code_post/blog_detail.html'


class YearArchiveView(BaseYearArchive):
    model = BlogPost


class MonthArchiveView(BaseMonthArchive):
    model = BlogPost