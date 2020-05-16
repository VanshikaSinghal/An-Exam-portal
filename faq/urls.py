from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.faqhome,name='faqhome'),
    path('<str:slug>', views.faqPost,name='faqPost')
]