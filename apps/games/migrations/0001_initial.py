# Generated by Django 5.0.1 on 2024-01-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_1_card_num', models.CharField(blank=True, max_length=2, null=True)),
                ('user_2_card_num', models.CharField(blank=True, max_length=2, null=True)),
                ('status', models.BooleanField(default=False)),
                ('rule', models.CharField(choices=[('bigger', '큰 숫자가 이기는 룰'), ('smaller', '작은 숫자가 이기는 룰')], default='', max_length=10)),
            ],
        ),
    ]
