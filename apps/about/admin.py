from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.about.models import Chairman, Position, Management, Predisition, Vacancy, Resume, Volunteer, UserResume


@admin.register(Chairman)
class ChairmanModelAdmin(ModelAdmin):
    list_display = ('id', 'full_name')


@admin.register(Position)
class PositionModelAdmin(ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Management)
class ManagementModelAdmin(ModelAdmin):
    list_display = ('id', 'full_name')


@admin.register(Predisition)
class PredisitionModelAdmin(ModelAdmin):
    list_display = ('id', 'full_name')


@admin.register(Vacancy)
class VacancyModelAdmin(ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Resume)
class ResumeModelAdmin(ModelAdmin):
    list_display = ('id', 'full_name')


@admin.register(Volunteer)
class VolunteerModelAdmin(ModelAdmin):
    list_display = ('id', 'full_name')


@admin.register(UserResume)
class UserResumeModelAdmin(ModelAdmin):
    list_display = ('id', 'vacancy')
