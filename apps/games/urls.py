from django.urls import path
from .views import *

app_name = 'games'

urlpatterns = [
    path('list/', game_list, name='list'),
    path('detail/<int:pk>', game_detail, name='detail'),
    path('attack/', game_attack, name='attack'),
    path('delete/<int:pk>', game_delete, name='delete'),
    path('match/<int:pk>', game_match, name='match'),
    path('accept/<int:pk>', game_accept, name='accept')
]