from statistics import mode
from django.db import models
from datetime import datetime

class News_ID(models.Model):
    news = models.BigIntegerField(verbose_name="hackernews-Id", unique=True)
    fetched_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.news)