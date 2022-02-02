from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField

class News_ID(models.Model):
    news = models.BigIntegerField(verbose_name="hackernews-Id", unique=True)
    fetched_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.news)


class NewsItem(models.Model):
    id = models.OneToOneField(News_ID, primary_key=True, on_delete=models.CASCADE) # making this id as pk
    deleted = models.BooleanField(default=False)
    type = models.CharField(max_length=100)
    by = models.CharField(max_length=255, null=True, blank=True)
    dead = models.BooleanField(default=False)
    kids = ArrayField(ArrayField(models.IntegerField(null=True, blank=True)))
    parent = models.IntegerField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    descendants = models.IntegerField(null=True, blank=True)
    time = models.BigIntegerField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        id = News_ID.objects.get['news'] # getting the news id
        self.id = id # replacing the id as the news id
        super(NewsItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.id