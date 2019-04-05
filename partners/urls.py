from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='partners'),
    path('<int:partner_id>', views.partner, name='partner'),
    
]