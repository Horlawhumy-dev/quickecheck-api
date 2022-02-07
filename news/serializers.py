from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import HackerNewsID, QuickCheckItem, QuickCheckNews


class NewsItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuickCheckItem
        fields = "__all__"


class NewsIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = HackerNewsID
        fields = ('hackernews',)


class QuickCheckNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuickCheckNews
        fields = "__all__"