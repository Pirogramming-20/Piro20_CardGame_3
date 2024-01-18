from django import forms
from .models import Game

#user1이 공격하기를 눌렀을 때 폼
class AttackForm(forms.ModelForm):
    class Meta():
        model = Game
        fields = ('__all__')

#user2가 반격하기를 눌렀을 때 폼   
class CounterattackForm(forms.ModelForm):
    class Meta():
        model = Game
        fields = ('__all__')
        