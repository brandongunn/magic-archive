# Generated by Django 4.0.2 on 2022-04-21 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_remove_game_id_game_gameid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='games',
            new_name='Season1Game',
        ),
        migrations.RenameModel(
            old_name='game',
            new_name='Season2Game',
        ),
    ]
