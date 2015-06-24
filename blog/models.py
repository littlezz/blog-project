from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from slugify import slugify
from django.core.urlresolvers import reverse

from core.managers import PublishManager
from core.fields import MarkdownField




# Create your models here.


class Displayable(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True)

    objects = PublishManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.publish_date == None:
            self.publish_date = timezone.now()
        super().save()


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


SPECIE_CHOICES = (
    ('code', '技术相关'),
    ('blog', '文学')
)

class SpecieChoiceMixin(models.Model):
    specie = models.CharField(max_length=20, choices=SPECIE_CHOICES)

    class Meta:
        abstract = True



class Category(SpecieChoiceMixin, Slugged):

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('hi', kwargs={'specie': 'blog'})

class Tag(Slugged):
    pass


class BlogPost(SpecieChoiceMixin, Displayable, Slugged):
    content = MarkdownField()
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, related_name='blog_posts')
    custom_description = models.CharField(max_length=255, blank=True)
    auto_description = models.CharField(max_length=255, blank=True)


    class Meta:
        ordering = ['-update_time']
        get_latest_by = ['-update_time']

    def save(self, *args, **kwargs):
        self.auto_description = self.content[:100]

        super().save(*args, **kwargs)

    @property
    def description(self):
        return self.custom_description or self.auto_description

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
            'specie': self.specie
        }
        return reverse('blog_post_detail', kwargs=kwargs)

