from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.news.models import Category, Region, Post


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Region)
class RegionModelAdmin(ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Post)
class PostModelAdmin(ModelAdmin):
    list_display = ('id', 'title', 'views')

