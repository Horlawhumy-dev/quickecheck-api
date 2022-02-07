from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
import math


class HackerNewsID(models.Model):
    hackernews = models.BigIntegerField(unique=True, primary_key=True)
    fetched_at = models.DateTimeField(default=datetime.now())

    def save(self, *args, **kwargs):
        self.id = self.hackernews # replacing the id as the hackernews id
        super(HackerNewsID, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.hackernews)


class QuickCheckItem(models.Model):
    id = models.OneToOneField(HackerNewsID, primary_key=True, blank=True, on_delete=models.CASCADE) # making this id as primary key
    deleted = models.BooleanField(default=False)
    type = models.CharField(max_length=100)
    by = models.CharField(max_length=255, null=True, blank=True)
    dead = models.BooleanField(default=False)
    kids = ArrayField(ArrayField(models.BigIntegerField(unique=True, null=True, blank=True))) # array field to store the array of kids value from the API.
    parent = models.IntegerField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    descendants = models.IntegerField(null=True, blank=True)
    time = models.BigIntegerField(unique=True, null=True, blank=True, default=math.ceil((datetime.utcnow() - datetime(1970,1,1,0,0,0)).total_seconds()))

    def save(self, *args, **kwargs):
        id = HackerNewsID.objects.get('hackernews') # getting the news id
        self.id = id # replacing the id as the hackernews id
        super(QuickCheckItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.id


# This model will allow custom news to bes saved, and be posted to.
class QuickCheckNews(models.Model):
    type = models.CharField(max_length=100)
    by = models.CharField(max_length=255, null=True, blank=True,)
    kids = ArrayField(ArrayField(models.BigIntegerField(null=True, blank=True))) # array field to store the array of kids value from the API.
    parent = models.IntegerField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True,)
    score = models.IntegerField(null=True, blank=True)
    descendants = models.IntegerField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    time = models.BigIntegerField(unique=True, null=True, blank=True, default=math.ceil((datetime.utcnow() - datetime(1970,1,1,0,0,0)).total_seconds()))

    def __str__(self):
        return f"{self.by}" #formatting as => (user - my-story-headlines) for instance.