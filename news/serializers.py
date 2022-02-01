from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import News_ID
class NewsIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = News_ID
        fields = ('news',)
