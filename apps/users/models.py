from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username = 로그인 할 때 입력하는 아이디
    # name = 본인 실명
    name = models.CharField(max_length = 20, blank=False) 
    score = models.IntegerField(default = 0)