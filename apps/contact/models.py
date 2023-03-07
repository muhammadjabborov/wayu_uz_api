from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import CharField, EmailField
from phonenumber_field.modelfields import PhoneNumberField

from apps.helpers.models import BaseModel


class Contact(BaseModel):
    full_name = CharField(max_length=255)
    phone_number = PhoneNumberField(unique=True)
    email = EmailField(unique=True)
    message = RichTextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Contact Model'
        verbose_name_plural = 'Contact'
