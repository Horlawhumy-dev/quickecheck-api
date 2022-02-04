import json
from django.shortcuts import render
import requests
from  rest_framework import serializers
from .serializers import NewsIdSerializer, NewsItemSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import HackerNewsID, QuickCheckItem

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
        
        res = [int(id.strip()) for id in result] # list comprehension to strip each element of the data
        
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
    
    def get_data_from_API(self):
        latest = HackerNewsID.objects.all()[len(HackerNewsID.objects.all())-1].hackernews # getting latest id from db
       
        NEWS_URL = f'https://hacker-news.firebaseio.com/v0/item/{str(latest)}.json?print=pretty'
        
        headers = {'user-agent': 'quickcheck/0.0.1'} 
        response = requests.get(NEWS_URL, headers=headers)
        data = json.loads(response.text)

        return data

    def get(self, request, format=True):
        data = self.get_data_from_API()
        
        return Response(data, status=status.HTTP_201_CREATED)


    def post(self, request, format=True):
        data = self.get_data_from_API()

        serializer = NewsItemSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# def newsItem(request, pk):
#     news_id = News_ID.objects.all()
#     NEWS_URL = f'https://hacker-news.firebaseio.com/v0/item/{str(pk)}.json?print=pretty'
#     headers = {'user-agent': 'quickcheck/0.0.1'}
#     response = requests.get(NEWS_URL, headers=headers)
#     print(response.text)
#     return render()
#     # return render(request, 'templates')
