from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import News_ID, NewsItem


class NewsItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsItem
        fields = '__all__'
        lookup_field = 'id'

class NewsIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = News_ID
        fields = ('news',)
