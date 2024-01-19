from django.shortcuts import render, redirect
from .models import Game, User
from .forms import AttackForm, AcceptForm
from django.db.models import Q
import random
# Create your views here.

def game_attack(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            game = Game()
            game.user_1 = request.user
            form = AttackForm(request=request, instance=game)
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
                return redirect('games:list')
            else:
                # 폼이 유효하지 않은 경우
                ctx = {
                    "form": form
                }
                return render(request, 'games/games_attack.html', ctx)
    else:
        return redirect('users:login')

def game_match (request, pk):
    game = Game.objects.get (id = pk)
    firstCardNum = int(game.user_1_card_num)
    secondCardNum = int(game.user_2_card_num)
    if firstCardNum == secondCardNum:
        game.winner = None
        game.loser = None
        game.save()
        game_pk = game.pk
    
        return redirect ('games:detail', game_pk)
    if game.rule == 'bigger':
        if (firstCardNum > secondCardNum):
            game.user_2.score -= secondCardNum
            game.user_1.score += firstCardNum
            game.user_1.save()
            game.user_2.save()
            game.winner = game.user_1
            game.loser = game.user_2
        else:
            game.user_1.score -= firstCardNum
            game.user_2.score += secondCardNum
            game.user_1.save()
            game.user_2.save()
            game.winner = game.user_2
            game.loser = game.user_1                 
    else:
        if (firstCardNum < secondCardNum):
            game.user_2.score -= secondCardNum
            game.user_1.score += firstCardNum
            game.user_1.save()
            game.user_2.save()
            game.winner = game.user_1
            game.loser = game.user_2  
        else:
            game.user_1.score -= firstCardNum
            game.user_2.score += secondCardNum
            game.user_1.save()
            game.user_2.save()
            game.winner = game.user_2
            game.loser = game.user_1
    game.save()
    game_pk = game.pk
    
    return redirect ('games:detail', game_pk)
        
        
def game_list (request):
    games = Game.objects.filter(Q(user_1=request.user) | Q(user_2=request.user))
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
    
    elif request.user.name == game.user_1.name:
        return render (request, 'games/game_detail_wait.html', ctx)
    
    else:
        return render (request, 'games/game_detail_defense.html', ctx)

def game_accept(request, pk):
    game = Game.objects.get(id=pk)
    if request.user.is_authenticated and request.user == game.user_2 and not game.status:
        if request.method == 'POST':
            form = AcceptForm(request.POST, instance=game)
            if form.is_valid():
                form.save()
                game.status = True
                game.save()
                return redirect('games:match', pk)
            else:
                print(form.errors)
        else:
            form = AcceptForm(request=request, instance=game)
        
            ctx = {'form': form, 'game': game}
            return render(request, 'games/games_accept.html', ctx)
    else:
        return redirect ('users:login')
            
def game_list (request):
    games = Game.objects.filter(Q(user_1=request.user) | Q(user_2=request.user))
    games = games.order_by('-id')
    ctx = {'games' : games}
    return render(request, 'games/game_list.html', ctx) 
       
def game_delete (request,pk):
    if request.method == 'POST':
        Game.objects.get(id=pk).delete()
    return redirect('games:list')
