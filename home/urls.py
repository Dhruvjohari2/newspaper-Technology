from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='views'),
    path("about", views.about, name='about'),
    path("daily", views.daily, name='daily'),
    path("weekly",views.weekly, name='weekly'),
    path("contact", views.contact, name='contact'),
    path("articles", views.articles, name= 'articles'),
    path("views",views.views, name='views'),
    path('signup',views.handleSignup, name='handleSignup'),
    path('login',views.handleLogin, name='handleLogin'),
    path('logout',views.handleLogout, name='handlelogout'),
 ]
