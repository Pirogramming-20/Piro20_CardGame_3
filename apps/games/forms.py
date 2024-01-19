from django import forms
from .models import Game, User
from django.core.exceptions import ValidationError
import random

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
        self.fields['user_2'].label = '공격 상대'
        
        # __init__에서 랜덤으로 선택된 숫자를 choices로 설정
        self.set_choices()

    def set_choices(self):
        if self.request is not None:
            # request가 존재하고 request=request로 호출된 경우에만 choices 업데이트
            # 랜덤으로 1부터 10까지 5개의 숫자 선택
            random_numbers = sorted(random.sample(range(1, 11), 5))
            choices = [(str(num), str(num)) for num in random_numbers]
            # 'user_1_card_num' 필드에 선택된 숫자를 사용할 수 있도록 설정
            self.fields['user_1_card_num'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect, label="내 카드 숫자")

    def clean(self):
        cleaned_data = super().clean()
        user_2 = cleaned_data.get('user_2')
        user_1_card_num = cleaned_data.get('user_1_card_num')

        if user_1_card_num is None:
            raise ValidationError('user_1_card_num is required.')

        if user_2 == self.instance.user_1:
            raise ValidationError('You cannot select user_1 as user_2.')

        # 나머지 validation 코드...

        return cleaned_data
    
class AcceptForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['user_2_card_num']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AcceptForm, self).__init__(*args, **kwargs)

        # __init__에서 랜덤으로 선택된 숫자를 choices로 설정
        self.set_choices()

    def set_choices(self):
        if self.request is not None:
            # request가 존재하고 request=request로 호출된 경우에만 choices 업데이트
            # 랜덤으로 1부터 10까지 5개의 숫자 선택
            random_numbers = sorted(random.sample(range(1, 11), 5))
            choices = [(str(num), str(num)) for num in random_numbers]

            # 'user_2_card_num' 필드에 선택된 숫자를 사용할 수 있도록 설정
            self.fields['user_2_card_num'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect, label="내 카드 숫자")

    def clean(self):
        cleaned_data = super().clean()
        user_2_card_num = cleaned_data.get('user_2_card_num')

        # 나머지 validation 코드...

        return cleaned_data