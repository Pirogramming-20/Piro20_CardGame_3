from django.shortcuts import render, redirect
from .models import Game, User
from .forms import AttackForm
from django.db.models import Q
# Create your views here.

def game_detail (request, pk):
    game = Game.objects.get(id = pk)
    if game.status:
        ctx = {
            'game': game
        }
        return render (request, 'games/games_detailmatch.html', ctx)
    

def game_create (request):
    if request.user.is_authenticated:
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
    else:
        return redirect ('users:login')


# Create your views here.
def game_list (request):
    now_user = User.objects.get(id=1)
    games = Game.objects.filter(Q(user_1=now_user) | Q(user_2=now_user))
    ctx = {'games' : games, 'now_user':now_user}
    return render(request, 'games/game_list.html', ctx)


def game_delete (request,pk):
    if request.method == 'POST':
        Game.objects.get(id=pk).delete()
    return redirect('games:list')
