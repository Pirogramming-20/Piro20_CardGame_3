# Generated by Django 5.0.1 on 2024-01-19 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_name_filled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name_filled',
        ),
    ]
