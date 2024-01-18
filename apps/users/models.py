from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username = 로그인 할 때 입력하는 아이디
    # name = 본인 실명
    name = models.CharField(max_length = 20, blank=False)
    score = models.IntegerField(default = 0)

# from allauth.account.signals import user_signed_up
# from django.dispatch import receiver

# @receiver(user_signed_up)
# def set_user_name(request, user, **kwargs):
#     # Google 계정의 이름을 가져와서 User 모델의 name 필드에 저장합니다.
#     # Google 계정의 이름은 'first_name' 'last_name' 형태입니다.
#     user.name = f'{user.first_name} {user.last_name}'
#     user.save()

