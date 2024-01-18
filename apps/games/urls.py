from django.urls import path
from .views import *

app_name = 'games'

urlpatterns = [
    path('list/', game_list, name='list'),

    path('attack/', attack, name='attack'),
    path('wait/', game_wait, name='wait'),

    path('defense/', game_defense, name='defense'),#대응하기 버튼 있는 페이지
    path('counterattack/', game_counterattack, name='counterattack'),#반격하기 페이지

    path('detail/', game_detail, name='detail'),#게임정보
]