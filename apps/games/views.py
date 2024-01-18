from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Game, User


# Create your views here.
def game_list (request):
    now_user = User.objects.get(id=1)
    games = Game.objects.filter(Q(user_1=now_user) | Q(user_2=now_user))
    ctx = {'games' : games, 'now_user':now_user}
    return render(request, 'games/game_list.html', ctx)

def game_detail (request):
    pass

def game_delete (request,pk):
    if request.method == 'POST':
        Game.objects.get(id=pk).delete()
    return redirect('games:list')
