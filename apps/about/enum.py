from django.db.models import TextChoices


class DaysWorkChoose(TextChoices):
    FULL_TIME = ('full_time', 'Full Time')
    PART_TIME = ('part_time', 'Part Time')
