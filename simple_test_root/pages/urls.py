# simple_test_root/pages/urls.py
from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('<str:pagename>/', views.index, name='index'),
    path('', views.index, name='index'),
]
