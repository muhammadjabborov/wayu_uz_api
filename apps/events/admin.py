from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.events.models import Category, Event


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Event)
class EventModelAdmin(ModelAdmin):
    list_display = ('title',)

