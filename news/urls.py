from django.urls import path
from .views import NewsIdView
urlpatterns = [
    path('all/', NewsIdView.as_view(), name='index')
]