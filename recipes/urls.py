from . import viewsfrom 
from django.urls import path


urlpatterns = [
    path('', views.Postlist.as_view(), name='home')
]