from django.db import models
from django.db.models import CharField, DecimalField, EmailField, URLField, ImageField
from phonenumber_field.modelfields import PhoneNumberField

from apps.helpers.models import BaseModel
from apps.home.enums import PaymentTypeChoose


class Donate(BaseModel):
    full_name = CharField(max_length=255)
    sum = DecimalField(max_digits=6, decimal_places=6)
    payment_type = CharField(max_length=25, choices=PaymentTypeChoose.choices, default=PaymentTypeChoose.PAYME)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Donate Model'
        verbose_name_plural = 'Donate'


class Location(BaseModel):
    latitude = DecimalField(max_digits=10, decimal_places=10)
    longitude = DecimalField(max_digits=10, decimal_places=10)
    phone_number = PhoneNumberField(unique=True)
    email = EmailField(unique=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Location Model'
        verbose_name_plural = 'Location'


class UseFulLinks(BaseModel):
    icon = ImageField(upload_to='photos/%Y/%m/%d/')
    title = CharField(max_length=255)
    link = URLField()

    def __str__(self):
        return self.title


class InstagramPost(BaseModel):
    post = ImageField(upload_to='media/posts/')
    url_address = URLField()

    class Meta:
        verbose_name = 'InstagramPost Model'
        verbose_name_plural = 'InstagramPost'
