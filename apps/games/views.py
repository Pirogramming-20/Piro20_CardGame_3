from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Game
from .forms import AttackForm

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
    if game.status:
        ctx = {
            'game': game
        }
        return render (request, 'games/games_detailmatch.html', ctx)
    
    

def game_create (request):
    if request.method == "GET":
        form = AttackForm()
        ctx = {
            "form": form
        }
        return render (request, 'games/games_create.html', ctx)
    form = AttackForm(request.POST)
    if form.is_valid():
        game_instance = form.save(commit=False)
        if game_instance.rule == 'bigger':
            if (game_instance.user_1_card_num > game_instance.user_2_card_num):
                game_instance.user_2.score -= game_instance.user_2_card_num
                game_instance.user_1.save()
                game_instance.user_2.save()
                game_instance.winner = game_instance.user_1
                game_instance.loser = game_instance.user_2
            else:
                game_instance.user_1.score -= game_instance.user_1_card_num
                game_instance.user_1.save()
                game_instance.user_2.save()
                game_instance.winner = game_instance.user_2
                game_instance.loser = game_instance.user_1
                
        else:
            if (game_instance.user_1_card_num < game_instance.user_2_card_num):
                game_instance.user_2.score -= game_instance.user_2_card_num
                game_instance.user_1.save()
                game_instance.user_2.save()
                game_instance.winner = game_instance.user_1
                game_instance.loser = game_instance.user_2  
            else:
                game_instance.user_1.score -= game_instance.user_1_card_num
                game_instance.user_1.save()
                game_instance.user_2.save()
                game_instance.winner = game_instance.user_2
                game_instance.loser = game_instance.user_1
    
        game_instance.save()
        game_pk = game_instance.pk
        return redirect ('games:detail', game_pk)
    else:
        return redirect ('games:list')
