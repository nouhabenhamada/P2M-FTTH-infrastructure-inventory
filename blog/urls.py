from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("login/", views.login_account, name='login'),
    path("signup/", views.signup),
    path("home/", views.home),
    path("new-post/", views.new_post),
    path("mypost/", views.mypost),
    path("signout/", views.sign_out),
    path('map/', views.map_page, name='map_page'),
]