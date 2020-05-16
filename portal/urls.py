"""stet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('contact', views.contact,name='contact'),
    path('about', views.about,name='about'),
    path('admitcard',views.admitview,name='admitcard'),
    path('register',views.register,name='register'),
    path('registerview',views.registerview,name='registerview'),
    path('instruction',views.instruction,name='instruction'),
    path('payment',views.payment,name='payment'),
    path('result1',views.result1,name='result'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('application',views.application,name='application'),
    path('handleregister',views.handleregister,name='handleregister'),
    path('handlelogin',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('handleimage',views.handleimage,name='handleimage'),
    path('result',views.resultdisplay,name='resultdisplay'),
    path('profile',views.profile,name='profile'),
   
    
]
