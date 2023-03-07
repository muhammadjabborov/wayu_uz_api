from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import CharField
from phonenumber_field.modelfields import PhoneNumberField

from apps.helpers.models import BaseModel


class FAQ(BaseModel):
    full_name = CharField(max_length=255)
    phone_number = PhoneNumberField()
    message = RichTextField()

    class Meta:
        verbose_name = 'FAQ Model'
        verbose_name_plural = 'FAQ'
