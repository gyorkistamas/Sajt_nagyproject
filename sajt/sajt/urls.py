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
from K_localization_framework import views as locale_views
from main import views
#from sajt import accounts
from accounts import views as acc_views

urlpatterns = [
    path('admin/', admin.site.urls)
    ,path('', views.index, name='index')
    ,path('accounts/3rdparty/login/cancelled/', acc_views.login_cancelled)
    ,path('accounts/', include("allauth.urls"))
    ,path('accounts/profile/', acc_views.profile, name='profile')
    ,path('about/', views.about, name='about')
    ,path('contact/', views.contact, name='contact')
    ,path('logout/', acc_views.logout_view, name='logout')
    ,path('login/', acc_views.login_view, name='login')
    ,path('register/', acc_views.reg_view, name='register')
    ,path('lost+password/', acc_views.lost_pwd_view, name='lost_pwd')
    ,path('reset-password/', acc_views.reset_pwd_view, name='reset_pwd')
    ,path('payment/', views.payment, name='payment')
    ,path('items/', views.items, name='items')
    ,path('add_to_cart/', views.add_to_cart, name="add_to_cart")
    ,path('cart/', views.cart_detail, name='cart_detail')
    ,path('cart/remove/', views.cart_remove, name='cart_remove')
    ,path('accounts/profile/edit/', acc_views.edit_profile, name='edit_profile')
    ,path('accounts/admin/', acc_views.admin, name='admin')
    ,path('accounts/admin/edit/email/<str:email>/', acc_views.admin_change_email, name='admin_change_email')
    ,path('accounts/admin/edit/saveUser/<int:userId>/', acc_views.admin_change_saveUser, name='admin_change_saveUser')
    ,path('accounts/admin/delete/<int:userId>/', acc_views.admin_change_deleteUser, name='admin_change_deleteUser')
    ,path('accounts/admin/translations/', locale_views.translation_list, name='translation_list')
    ,path('accounts/orders/order_detail', views.order_detail, name='order_detail')
    # ,path('accounts/admin/translations/add/', locale_views.translation_add, name='add_translation')
    # ,path('accounts/admin/translations/edit/<int:pk>/', locale_views.translation_edit, name='edit_translation')
    # ,path('accounts/admin/translations/delete/<int:pk>/', locale_views.translation_delete, name='delete_translation')
    # ,path('accounts/admin/translations/madd-add/', locale_views.mass_add_translation, name='mass_add_translation')
    # ,path('accounts/admin/translations/madd-edit/', locale_views.mass_edit_translation, name='mass_edit_translation')
    # ,path('accounts/admin/translations/madd-delete/', locale_views.mass_delete_translation, name='mass_delete_translation')
]
