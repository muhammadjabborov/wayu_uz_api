from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.home.models import Donate, Location, UseFulLinks, InstagramPost


@admin.register(Donate)
class DonateModelAdmin(ModelAdmin):
    list_display = ('id', 'full_name')


@admin.register(Location)
class LocationModelAdmin(ModelAdmin):
    list_display = ('id', 'phone_number')


@admin.register(UseFulLinks)
class UsefulLinksModelAdmin(ModelAdmin):
    list_display = ('id', 'title')


@admin.register(InstagramPost)
class InstagramPostModelAdmin(ModelAdmin):
    pass
