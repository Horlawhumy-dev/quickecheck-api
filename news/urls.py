from django.urls import path
from .views import NewsIdView, NewsItemView, QuickCheckNewsView, QuickCheckNewsRetrieveView, QuickCheckPostView

urlpatterns =[
    path('all/', NewsIdView.as_view(), name='index'), #127.0.0.1:8080/api/v0/items/all --> lists all news id
    path('item/', NewsItemView.as_view(), name='news-item'),  #127.0.0.1:8080/api/v0/items/item --> fetch latest news using latest id from db
    path('news/', QuickCheckNewsView.as_view(), name='quickecheknews'),  #127.0.0.1:8080/api/v0/ --> fetch latest news using latest id from db
    path('news/<str:pk>/', QuickCheckNewsRetrieveView.as_view(), name='quickecheknewsretrieve'),  #127.0.0.1:8080/api/v0/ --> update data with id specified
    path('post/', QuickCheckPostView.as_view(), name='quickecheknewsretrieve')  #127.0.0.1:8080/api/v0/ --> update data with id specified
]
 
# Search route
# http://127.0.0.1:8000/api/v0/items/news?search=this is a sample text 2

#Filter route
#http://127.0.0.1:8000/api/v0/items/news?type=comment