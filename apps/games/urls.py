from django.urls import path
from .views import *

app_name = 'games'

urlpatterns = [
    path('list/', game_list, name='list'),
    path('delete/<int:pk>', game_delete, name='delete'),
    path('detail/<int:pk>', game_detail, name='detail'),
    path('create/', game_create, name='create'),
]