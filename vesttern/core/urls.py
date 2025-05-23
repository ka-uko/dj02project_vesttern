from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('development/', views.development, name='development'),
    path('support/', views.support, name='support'),
    path('replication/', views.replication, name='replication'),
    path('portfolio/', views.portfolio, name='portfolio'),
]