from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username = 로그인 할 때 입력하는 아이디
    # name = 본인 실명
    class Meta:
        app_label = 'users' 

    name = models.CharField(max_length = 20, default='No Name')
    score = models.IntegerField(default = 0)

    def __str__ (self):
        return self.name
