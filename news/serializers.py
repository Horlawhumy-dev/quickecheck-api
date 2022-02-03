from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import HackerNewsID, QuickCheckItem


class NewsItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuickCheckItem
        fields = '__all__'
        # lookup_field = 'newsitem_id'

class NewsIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = HackerNewsID
        fields = ('hackernews_id',)
