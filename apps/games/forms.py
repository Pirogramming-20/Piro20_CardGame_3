from django import forms
from .models import Game, User
import random
class AttackForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['user_2', 'user_1_card_num']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AttackForm, self).__init__(*args, **kwargs)

    def clean_user_2(self):
        user_2 = self.cleaned_data.get('user_2')
        if user_2 == self.instance.user_1:
            raise forms.ValidationError('You cannot select user_1 as user_2.')
        return user_2
    
#user2가 반격하기를 눌렀을 때 폼   
class CounterattackForm(forms.ModelForm):
    class Meta():
        model = Game
        fields = ('__all__')
        