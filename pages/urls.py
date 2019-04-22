from django.urls import path
from django.shortcuts import redirect
from django.views.generic import RedirectView
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_list', PostListView.as_view(), name='post_list'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  
    path('workers', views.workers, name='workers'), 
    path('employers', views.employers, name='employers'), 
    path('howto', views.howto, name='howto'), 
    path('speak', views.speak, name='speak'), 
    path('search', views.search, name='search'),

] 
