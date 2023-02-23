from django.db import models
from .singleton_model import SingletonModel


class SiteSettings(SingletonModel):
    site_url = models.URLField(verbose_name='Website url', max_length=256)
    title = models.CharField(verbose_name='Title', max_length=256)

    def __str__(self):
        return 'Configuration'