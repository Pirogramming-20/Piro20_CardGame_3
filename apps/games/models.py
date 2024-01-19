from django.db import models
from apps.users.models import User
import random

class Game(models.Model):

    AVAILABLE_NUMBERS = sorted(random.sample(range(1, 11), 5))

    user_1_card_num = models.IntegerField(default = 0, choices=((num, str(num)) for num in AVAILABLE_NUMBERS))
    user_2_card_num = models.IntegerField(default = 0, choices=((num, str(num)) for num in AVAILABLE_NUMBERS))
    
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attackers')
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='defenders')
    
    # 랜덤으로 룰 지정
    RULE_CHOICES = [
        ('bigger', '큰 숫자가 이기는 룰'),
        ('smaller', '작은 숫자가 이기는 룰'),
    ]

    def random_rule():
        return random.choice(Game.RULE_CHOICES)

    status = models.BooleanField(default=False)
    rule = models.CharField(max_length=10, choices=RULE_CHOICES, default=random_rule)
    
    winner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='winner_games')
    loser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='loser_games')