# Generated by Django 4.0.2 on 2022-02-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('gameid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('date', models.CharField(max_length=25)),
                ('p1', models.CharField(max_length=50)),
                ('p1c', models.CharField(max_length=50)),
                ('p2', models.CharField(max_length=50)),
                ('p2c', models.CharField(max_length=50)),
                ('p3', models.CharField(max_length=50)),
                ('p3c', models.CharField(max_length=50)),
                ('p4', models.CharField(max_length=50)),
                ('p4c', models.CharField(max_length=50)),
                ('p5', models.CharField(max_length=50)),
                ('p5c', models.CharField(max_length=50)),
                ('winner', models.CharField(max_length=50)),
            ],
        ),
    ]