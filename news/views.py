import json
from rest_framework.reverse import reverse
from django.shortcuts import render
import requests
from django.http import Http404
from  rest_framework import serializers
from .serializers import NewsIdSerializer, NewsItemSerializer, QuickCheckNewsSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import HackerNewsID, QuickCheckItem, QuickCheckNews
from .pagination import QuickCheckNewsSetPagination




class NewsIdView(APIView):
    permission_classes = [AllowAny]

# GET list of all news ids from hackernews
    def get(self, request, format=None):

        NEWS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
        
        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL, headers=headers)

        result = response.text.split(',')[1:len(response.text.split(','))-2]  # in order to trim the last element
        last = response.text.split(',')[-1]  #got this from API " 499287535 ] /n" --> reshaped to that below
        result.insert(len(result), last.strip().split()[0]) # "499287535"
        
        res = [int(id.strip()) for id in result] # list comprehension to strip each element of the data
        
        return Response(res, status=status.HTTP_200_OK)

        

class NewsItemView(APIView):
    permission_classes = [AllowAny]

    def get_data_from_API(self):
        """
            This helps to return 
            formatted data fetched from endpoint provided
            using request.
        """
        # latest = HackerNewsID.objects.all()[len(HackerNewsID.objects.all())-1].hackernews # getting latest id from db
        result = []
        half = 0
        total = len(HackerNewsID.objects.all()) # getting the total ids from the db

        #slicing into half based on even or odd total
        if total % 2 == 0:
            half = len(HackerNewsID.objects.all()) / 2
        else:
            half = (len(HackerNewsID.objects.all()) / 2) + 1

        ids = HackerNewsID.objects.all()[:half] #slicing the queryset to get last half

        for id in ids:
            NEWS_URL = f'https://hacker-news.firebaseio.com/v0/item/{str(id)}.json?print=pretty'
            headers = {'user-agent': 'quickcheck/0.0.1'} 
            response = requests.get(NEWS_URL, headers=headers)
            data = json.loads(response.text)
            result.append(data)

        return result

    
#GET the latest hackernews streamed
    def get(self, request, format=None):
        return Response(self.get_data_from_API(),status=status.HTTP_201_CREATED)


class QuickCheckNewsView(ListAPIView):
    queryset = QuickCheckNews.objects.all() #queryset of data from database

    serializer_class = QuickCheckNewsSerializer

    permission_classes = [AllowAny] # permission to view the API

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['type'] #filter by type options

    filter_backends = [filters.SearchFilter] 

    search_fields = ['text'] # filter by text search

    pagination_class = QuickCheckNewsSetPagination
    

    def post(self, request, format=None):
        serializer = QuickCheckNewsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


class QuickCheckNewsRetrieveView(APIView):
    
    def get_object(self, pk):
        try:
            return QuickCheckNews.objects.get(pk=pk)
        except QuickCheckNews.DoesNotExist:
            raise Http404

    
    def get(self, request, pk, format=None):
        quickchecknews = self.get_object(pk)
        serializer = QuickCheckNewsSerializer(quickchecknews)
        if serializer:
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, format=None):
        quickchecknews = self.get_object(pk)
        serializer = QuickCheckNewsSerializer(quickchecknews, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        quickchecknews = self.get_object(pk)
        if quickchecknews:
            quickchecknews.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("Invalid data!", status=status.HTTP_404_NOT_FOUND)