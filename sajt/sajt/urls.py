"""
URL configuration for sajt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from re import template
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from main import views
#from sajt import accounts
from accounts import views as acc_views

urlpatterns = [
    path('admin/', admin.site.urls)
    ,path('', views.index, name='index')
    ,path('accounts/3rdparty/login/cancelled/', acc_views.login_cancelled)
    ,path('accounts/', include("allauth.urls"))
    ,path('logout/', acc_views.logout_view, name='logout')
    ,path('login/', acc_views.login_view, name='login')
    ,path('register/', acc_views.reg_view, name='register')
    ,path('payment/', views.payment, name='payment')
]
