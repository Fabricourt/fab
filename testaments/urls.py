from django.urls import path
from .views import (
    PotListView,
    PotDetailView,
    PotCreateView,
    PotUpdateView,
    PotDeleteView,
    UserPotListView
)
from . import views

urlpatterns = [
    path('pot_list', PotListView.as_view(), name='pot_list'),
    path('user/<str:username>', UserPotListView.as_view(), name='user-pots'),
    path('pot/<int:pk>/', PotDetailView.as_view(), name='pot-detail'),
    path('pot/new/', PotCreateView.as_view(), name='pot-create'),
    path('pot/<int:pk>/update/', PotUpdateView.as_view(), name='pot-update'),
    path('pot/<int:pk>/delete/', PotDeleteView.as_view(), name='pot-delete'),
   
 
]