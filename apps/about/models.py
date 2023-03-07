from ckeditor.fields import RichTextField
from datetime import datetime
from django.db.models import CharField, ImageField, IntegerField, SlugField, ForeignKey, PROTECT, EmailField, \
    DecimalField, SET_NULL, FileField, DateField
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from thumbnails.fields import ImageField
from apps.about.enum import DaysWorkChoose
from apps.helpers.models import BaseModel


class Chairman(BaseModel):
    full_name = CharField(max_length=255)
    image = ImageField(upload_to='photos/%Y/%m/%d/')
    get_thumbnails = ImageField(pregenerated_sizes=["small", "large", "medium"])
    description = RichTextField(null=True)
    address = CharField(max_length=255)
    year = DateField(default=datetime.now().date())
    position = CharField(max_length=255)
    phone_number = PhoneNumberField(unique=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Chairman Model'
        verbose_name_plural = 'Chairman'
        ordering = ['-created_at']


class Position(BaseModel):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Position Model'
        verbose_name_plural = 'Position'
        ordering = ['-created_at']


class Management(BaseModel):
    full_name = CharField(max_length=255)
    position = ForeignKey('about.Position', PROTECT)
    image = ImageField(upload_to='photos/%Y/%m/%d/')
    get_thumbnails = ImageField(pregenerated_sizes=["small", "large", "medium"])
    days = CharField(max_length=255)
    phone_number = PhoneNumberField(unique=True, null=True)
    email = EmailField(unique=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Management Model'
        verbose_name_plural = 'Management'
        ordering = ['-created_at']


class Predisition(BaseModel):
    full_name = CharField(max_length=255)
    image = ImageField(upload_to='photos/%Y/%m/%d/')
    get_thumbnails = ImageField(pregenerated_sizes=["small", "large", "medium"])
    country = CountryField(default='UZB')
    description = RichTextField()
    phone_number = PhoneNumberField(unique=True)
    email = EmailField(unique=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Predisition Model'
        verbose_name_plural = 'Predisition'
        ordering = ['-created_at']


class Vacancy(BaseModel):
    title = CharField(max_length=255)
    salary = DecimalField(max_digits=6, default=0, decimal_places=6)
    phone_number = PhoneNumberField(unique=True)
    days_work = CharField(max_length=25, choices=DaysWorkChoose.choices, default=DaysWorkChoose.FULL_TIME)
    description = RichTextField()


class Resume(BaseModel):
    vacancy = ForeignKey('about.Vacancy', SET_NULL, null=True, blank=True)
    full_name = CharField(max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField()
    resume = FileField(upload_to='resume/%Y/%m/%d/')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Resume Model'
        verbose_name_plural = 'Resume'
        ordering = ['-created_at']


class Volunteer(BaseModel):
    full_name = CharField(max_length=255)
    email = EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True)
    file = FileField(upload_to='files/%Y/%m/%d/')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Volunteer Model'
        verbose_name_plural = 'Volunteer'
        ordering = ['-created_at']


class UserResume(BaseModel):
    vacancy = ForeignKey('about.Vacancy', SET_NULL, null=True)
    resume = ForeignKey('about.Resume', SET_NULL, null=True)

    def __str__(self):
        return f'{self.resume} on {self.vacancy}'

    class Meta:
        verbose_name = 'User Resume Model'
        verbose_name_plural = 'User Resume'
        ordering = ['-created_at']
