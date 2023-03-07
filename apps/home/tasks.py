from celery import shared_task

from apps.home.models import InstagramPost
from apps.home.scrapper import web_scraping


@shared_task(name='get_instgram_posts')
def get_instagram_posts():
    # InstagramPost.objects.all().delete()
    web_scraping()
