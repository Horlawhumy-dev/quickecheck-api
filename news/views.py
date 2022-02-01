import re
from urllib import response
from django.shortcuts import render
import requests
from .serializers import NewsIdSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import News_ID

class NewsIdView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        NEWS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL, headers=headers)
        result = response.text.split(',')[1:499] 
        last = response.text.split(',')[-1]  # " 499287535 ] /n" -> reshaped to that below
        result.insert(len(result), last.strip().split()[0]) # "499287535"
        res = [int(id.strip()) for id in result] # list comprehension
        return Response(res)

        
    # def post(self, request, format=None):
    #     serializer = NewsIdSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class NewsView(APIView):
    permission_classes = [AllowAny]
  
    def get(self, request, format=None):
          news_id = News_ID.objects.all()
          for id in news_id:
            NEWS_URL = f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty'
            headers = {'user-agent': 'quickcheck/0.0.1'}
            response = requests.get(NEWS_URL, headers=headers)
        # result = response.text.split(',')[1:499] 
        # last = response.text.split(',')[-1]  # " 499287535 ] /n" -> reshaped to that below
        # result.insert(len(result), last.strip().split()[0]) # "499287535"
        # res = [int(id.strip()) for id in result] # list comprehension
            return Response(response.text)


# def index(request):
#     result = []
#     NEWS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
#     headers = {'user-agent': 'quickcheck/0.0.1'}
#     response = requests.get(NEWS_URL, headers=headers)
#     print(response.text[:10])
#     # for id in response.text[10]:
#     #     NEWS_URL_ID = f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty'
#     #     item = requests.get(NEWS_URL_ID)
#     #     result.append(item)
#     # print(result)
#     return render(request, 'templates/')
