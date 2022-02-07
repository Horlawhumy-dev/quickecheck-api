from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import HackerNewsID, QuickCheckItem, QuickCheckNews


class NewsItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuickCheckItem
        fields = "__all__"
        # fields = ('id', 'type', 'deleted', 'by', 'dead', 'parent', 'text', 'url', 'title', 'score', 'descendants', 'time', 'kids')
        # lookup_field = 'id'
    
    # def create(self, validated_data):
    #     # if 'id' in validated_data:
    #     #     latest = QuickCheckItem.objects.all()[len(QuickCheckItem.objects.all())-1].id + 1
    #     #     validated_data['id'] = latest
    #     return QuickCheckItem.objects.create(**validated_data)


class NewsIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = HackerNewsID
        fields = ('hackernews',)


class QuickCheckNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuickCheckNews
        fields = "__all__"
        # fields = ['id', 'type', 'by', 'kids', 'parent', 'text', 'url', 'title', 'score', 'descendants','deleted', 'time']