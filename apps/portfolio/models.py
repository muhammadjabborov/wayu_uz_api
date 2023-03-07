from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import CharField, FileField, ForeignKey, PROTECT, EmailField, CASCADE
from thumbnails.fields import ImageField

from apps.helpers.models import BaseModel


class Document(BaseModel):
    title = CharField(max_length=255)
    file = FileField(upload_to='docs/')

    def __str__(self):
        return self.title


class Member(BaseModel):
    full_name = CharField(max_length=255)
    image = ImageField(upload_to='photos/%Y/%m/%d/')
    get_thumbnails = ImageField(pregenerated_sizes=["small", "large", "medium"])
    email = EmailField(unique=True)

    def __str__(self):
        return self.full_name


class Project(BaseModel):
    icon = ImageField(upload_to='icons/%Y/%m/%d/')
    title = CharField(max_length=255)
    image = ImageField(upload_to='photos/%Y/%m/%d/')
    get_thumbnails = ImageField(pregenerated_sizes=["small", "large", "medium"])
    documents = ForeignKey('portfolio.Document', PROTECT)
    member = ForeignKey('portfolio.Member', PROTECT)
    description = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project Model'
        verbose_name_plural = 'Project'


class Form(BaseModel):
    full_name = CharField(max_length=255)
    email = EmailField(unique=True)
    message = RichTextField()
    project = ForeignKey('portfolio.Project', CASCADE)

    def __str__(self):
        return self.full_name












