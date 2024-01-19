from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Game
from .forms import AttackForm
import random

# Create your views here.
def game_list (request):
    games = Game.objects.filter(Q(user_1=request.user) | Q(user_2=request.user))
    print('여기보세요',games)
    ctx = {'games' : games}
    return render(request, 'games/game_list.html', ctx)

def game_delete (request,pk):
    if request.method == 'POST':
        Game.objects.get(id=pk).delete()
    return redirect('games:list')

def game_detail (request, pk):
    game = Game.objects.get(id = pk)
    ctx = {
            'game': game
    }
    if game.status:
        return render (request, 'games/game_detail_match.html', ctx)
    
    elif request.user.name == game.player_1.name:
        return render (request, 'games/game_detail_wait.html', ctx)
    
    else:
        return render (request, 'games/game_detail_defense.html', ctx)

def game_attack(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            game = Game()
            game.user_1 = request.user
            form = AttackForm(request=request, instance=game)  # 폼에 기존 게임 정보를 넘겨줍니다.
            ctx = {
                "form": form
            }
            return render(request, 'games/games_attack.html', ctx)
        elif request.method == "POST":
            game = Game()
            game.user_1 = request.user
            form = AttackForm(request.POST, instance=game)
            if form.is_valid():
                form.save()
            return redirect ('games:list')
    else:
        return redirect('users:login')

def game_match (request, pk):
    game = Game.objects.get (id = pk)
    if game.rule == 'bigger':
        if (game.user_1_card_num > game.user_2_card_num):
            game.user_2.score -= game.user_2_card_num
            game.user_1.save()
            game.user_2.save()
            game.winner = game.user_1
            game.loser = game.user_2
        else:
            game.user_1.score -= game.user_1_card_num
            game.user_1.save()
            game.user_2.save()
            game.winner = game.user_2
            game.loser = game.user_1
                    
    else:
        if (game.user_1_card_num < game.user_2_card_num):
            game.user_2.score -= game.user_2_card_num
            game.user_1.save()
            game.user_2.save()
            game.winner = game.user_1
            game.loser = game.user_2  
        else:
            game.user_1.score -= game.user_1_card_num
            game.user_1.save()
            game.user_2.save()
            game.winner = game.user_2
            game.loser = game.user_1
    game.save()
    game_pk = game.pk
    return redirect ('games:detail', game_pk)

def game_accept (request, pk):
    game = Game.objects.get (id = pk)
    if request.user.is_authenticated:
        if request.user == game.user_2:
            if game.status == False:          
                game.status = True
                game.user_2_card_num = random.randint(1,11)
                game.save()
                return redirect ('games:match', pk)
