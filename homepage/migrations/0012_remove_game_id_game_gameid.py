# Generated by Django 4.0.2 on 2022-04-21 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_remove_game_gameid_game_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='id',
        ),
        migrations.AddField(
            model_name='game',
            name='gameid',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]