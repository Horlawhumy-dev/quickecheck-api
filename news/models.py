from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField

class HackerNewsID(models.Model):
    hackernews = models.BigIntegerField(unique=True)
    fetched_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.hackernews)


class QuickCheckItem(models.Model):
    id = models.OneToOneField(HackerNewsID, primary_key=True, blank=True, on_delete=models.CASCADE) # making this id as primary key
    deleted = models.BooleanField(default=False)
    type = models.CharField(max_length=100)
    by = models.CharField(max_length=255, null=True, blank=True)
    dead = models.BooleanField(default=False)
    kids = ArrayField(ArrayField(models.IntegerField(blank=True)), default=list) # array field to store the array of kids value from the API.
    parent = models.IntegerField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    descendants = models.IntegerField(null=True, blank=True)
    time = models.BigIntegerField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        id = HackerNewsID.objects.get['hackernews'] # getting the news id
        self.id = id # replacing the id as the news id
        super(QuickCheckItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.id