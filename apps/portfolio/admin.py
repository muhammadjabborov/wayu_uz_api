from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.portfolio.models import Document, Member, Project, Form


@admin.register(Document)
class DocumentModelAdmin(ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Member)
class MemberModelAdmin(ModelAdmin):
    list_display = ('id', 'full_name')


@admin.register(Project)
class ProjectModelAdmin(ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Form)
class FormModelAdmin(ModelAdmin):
    list_display = ('id', 'full_name')
