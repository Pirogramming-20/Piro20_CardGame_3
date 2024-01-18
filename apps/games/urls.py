from django.urls import path
from .views import *

app_name = 'games'

urlpatterns = [
    path('list/', game_list, name='list'),
    path('detail/', game_detail, name='detail'),#게임정보
    path('delete/<int:pk>', game_delete, name='delete'),
]