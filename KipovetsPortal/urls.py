"""KipovetsPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from news.views import PostView, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, IndexView
from news.models import Post
from accounts.views import upgrade_me

urlpatterns = [
    path("admin/", admin.site.urls),
    path('news/', PostView.as_view(queryset=Post.objects.filter(type_post='NW')), name='postlist'),
    path('articles/', PostView.as_view(queryset=Post.objects.filter(type_post='AR')), name='postlist'),
    path('news/<int:pk>/', PostDetail.as_view(), name='post'),
    path('articles/<int:pk>/', PostDetail.as_view(), name='post'),
    path('news/search/', PostSearch.as_view(), name='search'),
    path('news/create/', PostCreate.as_view(), name='create'),
    path('articles/create/', PostCreate.as_view(), name='create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='edit'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='edit'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='edit'),
    path('accounts/', include('allauth.urls')),
    path('', IndexView.as_view(), name='index'),
    path('accounts/upgrade/', upgrade_me, name='upgrade'),
]
