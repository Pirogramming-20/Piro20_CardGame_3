from django.db import models
import random

# Create your models here.
class Game(models.Model):

    #랜덤으로 숫자 5개 만들기
    def generate_random_num():
        nums = random.sample(range(1,11), 5)
        return [(num, f'{num}') for num in nums]
    
    user_1_NUMS_CHOICE = generate_random_num()
    user_2_NUMS_CHOICE = generate_random_num()
    
    user_1_card_num = models.CharField(max_length=10, choices=user_1_NUMS_CHOICE, null=True)
    user_2_card_num = models.CharField(max_length=10, choices=user_2_NUMS_CHOICE, null=True)

    #랜덤으로 룰 지정
    RULE_CHOICES = [
        ('bigger', '큰 숫자가 이기는 룰'),
        ('smaller', '작은 숫자가 이기는 룰'),
    ]

    rule = models.CharField(max_length=10, choices=RULE_CHOICES, default=random.choice(RULE_CHOICES))
    # user_1 = 
    # user_2 =
    # winner ??????
    # loser ?????
