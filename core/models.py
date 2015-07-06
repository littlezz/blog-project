from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from slugify import slugify
from django.core.urlresolvers import reverse
from .managers import PublishManager
from django.utils.text import Truncator



class Displayable(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True)

    objects = PublishManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.publish_date = self.publish_date or timezone.now()
        super().save(*args, **kwargs)



class Slugged(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        self.slug = self.unique_slug(self.slug)
        super().save(*args, **kwargs)


    def unique_slug(self, slug:str):
        i = 0
        queryset = self.__class__._default_manager.exclude(id=self.id)
        old_slug = slug.strip('-')
        while True:
            try:
                obj = queryset.get(slug=slug)
            except ObjectDoesNotExist:
                return slug
            else:
                slug = '{}-{}'.format(old_slug, i)
                i += 1





class AbstractTag(Slugged):
    name_space = None
    class Meta:
        abstract = True

    def get_absolute_url(self):
        kwargs = {
            'tag': self.slug
        }
        return reverse(':'.join((self.name_space, 'blog_list_by_tag')), kwargs=kwargs)

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains",)


class AbstractCategory(Slugged):
    name_space = None
    class Meta:
        abstract = True

    def get_absolute_url(self):
        kwargs = {
            'category_slug': self.slug
        }
        return reverse(':'.join((self.name_space, 'blog_list_by_category')), kwargs=kwargs)



class BaseBlogPost(Displayable, Slugged):
    tags = models.ManyToManyField("Tag", blank=True)
    category = models.ForeignKey("Category", blank=True, null=True, on_delete=models.SET_NULL, related_name='blog_posts')
    custom_description = models.CharField(max_length=255, blank=True)
    auto_description = models.TextField(blank=True)
    feature_image = models.ImageField(blank=True, null=True)
    name_space = None
    description_trunc_num = 300

    class Meta:
        ordering = ['-update_time']
        get_latest_by = ['-publish_date']
        abstract = True

    def save(self, *args, **kwargs):
        self.auto_description = self.generate_auto_description()
        super().save(*args, **kwargs)

    @property
    def description(self):
        return self.custom_description or self.auto_description



    def rendered_content(self):
        """
        must rewrite when use markdown content field.
        输出渲染好的安全的带html tag的内容。
        """
        return self.content

    def generate_auto_description(self):
        """
        从渲染好的文本里面截取
        """
        content = self.rendered_content()

        return Truncator(content).words(self.description_trunc_num, html=True, truncate=' ...')

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,

        }
        return reverse(self.name_space + ':' + 'blog_post_detail', kwargs=kwargs)



