from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('youtube/', views.youtube, name='youtube'),
    path('game/', views.game, name='game'),
    path('shop/', views.shop, name='shop'),
    path('trends/', views.trends, name='trends')
]
