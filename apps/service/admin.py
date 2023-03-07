from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.service.models import FAQ


@admin.register(FAQ)
class FaqModelAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number')
