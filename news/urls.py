from django.urls import path
from .views import NewsIdView, NewsItemView
urlpatterns = [
    path('all/', NewsIdView.as_view(), name='index'), #127.0.0.1:8080/1pi/v0/all --> lists all news id
    path('item/', NewsItemView.as_view(), name='news-item')  #127.0.0.1:8080/1pi/v0/all --> fetch latest news using latest id from db
]