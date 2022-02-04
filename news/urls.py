from django.urls import path
from .views import NewsIdView, NewsItemView, QuickCheckNewsView
urlpatterns = [
    path('all/', NewsIdView.as_view(), name='index'), #127.0.0.1:8080/api/v0/items/all --> lists all news id
    path('item/', NewsItemView.as_view(), name='news-item'),  #127.0.0.1:8080/api/v0/items/item --> fetch latest news using latest id from db
    path('news/', QuickCheckNewsView.as_view(), name='quickecheknews')  #127.0.0.1:8080/api/v0/ --> fetch latest news using latest id from db
]