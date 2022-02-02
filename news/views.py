import json
from urllib import response
from django.shortcuts import render
import requests
from .serializers import NewsIdSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import News_ID, NewsItem

# GET list of all news ids from hackernews
class NewsIdView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        NEWS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL, headers=headers)
        result = response.text.split(',')[1:len(response.text.split(','))-2]  # in order to trim the last element
        last = response.text.split(',')[-1]  #got this from API " 499287535 ] /n" --> reshaped to that below
        result.insert(len(result), last.strip().split()[0]) # "499287535"
        res = [int(id.strip()) for id in result] # list comprehension
        return Response(res)

        
    # def post(self, request, format=None):
    #     serializer = NewsIdSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class NewsItemView(RetrieveAPIView):
    permission_classes = [AllowAny]
    lookup_field = 'id'
    
    def get(self, request, format=True):
        latest = News_ID.objects.all()[len(News_ID.objects.all())-1].news # getting latest id from db
        NEWS_URL = f'https://hacker-news.firebaseio.com/v0/item/{str(latest)}.json?print=pretty'
        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL, headers=headers)
        data = json.loads(response.text)
        return Response(data)


# def newsItem(request, pk):
#     news_id = News_ID.objects.all()
#     NEWS_URL = f'https://hacker-news.firebaseio.com/v0/item/{str(pk)}.json?print=pretty'
#     headers = {'user-agent': 'quickcheck/0.0.1'}
#     response = requests.get(NEWS_URL, headers=headers)
#     print(response.text)
#     return render()
#     # return render(request, 'templates')
