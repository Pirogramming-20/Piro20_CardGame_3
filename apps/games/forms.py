from django import forms
from .models import Game, User
from django.core.exceptions import ValidationError
import random
class AttackForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['user_2', 'user_1_card_num']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AttackForm, self).__init__(*args, **kwargs)
        current_user = self.instance.user_1
        self.fields['user_2'].queryset = User.objects.exclude(pk=current_user.pk)

    def clean(self):
        cleaned_data = super().clean()
        user_2 = cleaned_data.get('user_2')
        user_1 = self.instance.user_1  # 기존 게임 정보에서 user_1 가져오기

        if user_2 == user_1:
            raise ValidationError('You cannot select user_1 as user_2.')
#user2가 반격하기를 눌렀을 때 폼   
class AcceptForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['user_2_card_num']