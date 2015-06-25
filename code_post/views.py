from .models import BlogPost, Category
from core.views import BaseBlogDetailView, BaseBlogListView, BaseGetContextMixin


class GetContextMixin(BaseGetContextMixin):
    category = Category


class BlogListView(GetContextMixin, BaseBlogListView):
    queryset = BlogPost.objects.publish()
    model = BlogPost
    template_name = 'code_post/blog_list.html'





class BlogDetailView(GetContextMixin, BaseBlogDetailView):
    queryset = BlogPost.objects.publish()
    template_name = 'code_post/blog_detail.html'