from django.db import models

# Create your models here.
class Season1Game(models.Model):
    gameid=models.IntegerField(primary_key=True,unique=True)
    date=models.CharField(max_length=25)
    p1 = models.CharField(max_length=50)
    p1c = models.CharField(max_length=50)
    p2 = models.CharField(max_length=50)
    p2c = models.CharField(max_length=50)
    p3 = models.CharField(max_length=50)
    p3c = models.CharField(max_length=50)
    p4 = models.CharField(max_length=50)
    p4c = models.CharField(max_length=50)
    p5 = models.CharField(max_length=50)
    p5c = models.CharField(max_length=50)
    winner = models.CharField(max_length=50)

    def __str__(self):
        return str(self.gameid) + " " + self.date


class players(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    wins = models.IntegerField()
    losses = models.IntegerField()
    draws = models.IntegerField()

    def __str__(self):
        return self.pname + " : " + str(self.wins)+"-"+str(self.losses)+"-"+str(self.draws)

class commanders(models.Model):
    cname = models.CharField(max_length=100)
    cmc = models.IntegerField()
    color_identity = models.CharField(max_length=15)
    loyalty = models.CharField(null=True,blank=True, max_length=10)
    power = models.CharField(null=True,blank=True,max_length=10)
    toughness = models.CharField(null=True,blank=True,max_length=10)
    typeLine= models.CharField(max_length=100)

    def __str__(self):
        return self.cname

class comPlayed(models.Model):
    cname = models.CharField(max_length=50)
    pid = models.IntegerField()
    times = models.IntegerField()
    wins = models.IntegerField()

    def __str__(self):
        return self.cname + " : " + str(self.pid)

class Season2Game(models.Model):
    gameid = models.IntegerField(primary_key=True, unique=True)
    date = models.CharField(max_length=25)
    p1 = models.CharField(max_length=50)
    p1c = models.CharField(max_length=100)
    p2 = models.CharField(max_length=50)
    p2c = models.CharField(max_length=100)
    p3 = models.CharField(max_length=50)
    p3c = models.CharField(max_length=100)
    p4 = models.CharField(max_length=50)
    p4c = models.CharField(max_length=100)
    winner = models.CharField(max_length=50)

    def __str__(self):
        return str(self.gameid) + " " + self.date