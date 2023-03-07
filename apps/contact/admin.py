from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.contact.models import Contact


@admin.register(Contact)
class ContactModelAdmin(ModelAdmin):
    list_display = ('id', 'full_name')
