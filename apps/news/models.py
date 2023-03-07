from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField
from django.db.models import CharField, SlugField, ForeignKey, CASCADE, IntegerField
from thumbnails.fields import ImageField

from apps.helpers.models import BaseModel


class Category(BaseModel):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category Model'
        verbose_name_plural = 'Category'


class Region(BaseModel):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Region Model'
        verbose_name_plural = 'Region'


class Post(BaseModel):
    title = CharField(max_length=255)
    description = RichTextField()
    tags = ArrayField(CharField(max_length=255))
    image = ImageField(upload_to='photos/%Y/%m/%d/')
    get_thumbnails = ImageField(pregenerated_sizes=["small", "large", "medium"])
    views = IntegerField(default=0)
    region = ForeignKey('news.Region', CASCADE)
    category = ForeignKey('news.Category', CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(self, *args, **kwargs)
        else:
            self.views += 1
            super().save(self, *args, **kwargs)

    @property
    def get_post_by_category(self):
        event = Post.objects.filter(category=self.category)
        return event

    class Meta:
        verbose_name = 'Post Model'
        verbose_name_plural = 'Post'
