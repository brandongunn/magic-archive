# Generated by Django 4.0.2 on 2022-04-21 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='gameid',
        ),
        migrations.AddField(
            model_name='game',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
