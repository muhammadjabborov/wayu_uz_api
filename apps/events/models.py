from ckeditor.fields import RichTextField
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


class Event(BaseModel):
    title = CharField(max_length=255)
    slug = SlugField(unique=True)
    category = ForeignKey('events.Category', CASCADE)
    location = CharField(max_length=255)
    image = ImageField(upload_to='photos/%Y/%m/%d/')
    get_thumbnails = ImageField(pregenerated_sizes=["small", "large", "medium"])
    views = IntegerField(default=0)
    description = RichTextField()

    def __str__(self):
        return self.title

    @property
    def get_event_by_category(self):
        event = Event.objects.filter(category=self.category)
        return event

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(self, *args, **kwargs)
        else:
            self.views += 1
            super().save(self, *args, **kwargs)

    class Meta:
        verbose_name = 'Event Model'
        verbose_name_plural = 'Event'
