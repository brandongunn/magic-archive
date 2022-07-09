import csv, scrython, time
from django.db.models import F
from itertools import chain
from homepage.models import Season2Game
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt



#General Group Data

# total games played
def totalGames():
    return (int(Season2Game.objects.latest('gameid').gameid))

# turn order Wins
def turnOrderWins():
    player1wins = str(Season2Game.objects.filter(winner="Player 1").count())
    player2wins = str(Season2Game.objects.filter(winner="Player 2").count())
    player3wins = str(Season2Game.objects.filter(winner="Player 3").count())
    player4wins = str(Season2Game.objects.filter(winner="Player 4").count())
    return ("Wins based on turn order - 1st: "+ player1wins + ", 2nd: "+ player2wins +", 3rd: "+ player3wins +", 4th: "+ player4wins)

# Color Combos Played for All games/players
def colorIdentity():
    games = Season2Game.objects.all()
    colors = {"colorless": 0, "white": 0, "blue": 0, "black": 0, "red": 0, "green": 0,
              "azorius": 0, "dimir": 0, "rakdos": 0, "gruul": 0, "selesnya": 0, "orzhov": 0, "izzet": 0, "golgari": 0,
              "boros": 0, "simic": 0, "esper": 0, "grixis": 0, "jund": 0, "naya": 0, "bant": 0, "abzan": 0, "jeskai": 0
        , "sultai": 0, "mardu": 0, "temur": 0, "yore-tiller": 0, "glint-eye": 0, "dune-brood": 0, "ink-treader": 0
        , "witch-maw": 0, "5 color": 0}
    for game in games:
        colors[cardColor(game.p1c)] += 1
        colors[cardColor(game.p2c)] += 1
        colors[cardColor(game.p3c)] += 1
        if (game.p4c != "N/A"):
            colors[cardColor(game.p4c)] += 1
    return colors

# color identity Wins
def colorIdentityWins():
    games = Season2Game.objects.all()
    colors = {"colorless": 0, "white": 0, "blue": 0, "black": 0 , "red": 0 , "green": 0 ,
             "azorius": 0, "dimir":0, "rakdos":0, "gruul":0, "selesnya":0, "orzhov":0, "izzet":0, "golgari":0,
              "boros":0, "simic":0, "esper":0, "grixis":0, "jund":0, "naya":0, "bant":0, "abzan":0, "jeskai":0
        , "sultai":0, "mardu":0, "temur":0, "yore-tiller":0, "glint-eye":0, "dune-brood":0, "ink-treader":0
        , "witch-maw":0, "5 color":0  }
    for game in games:
        win = game.winner
        winningCommander = ""
        if (win=="Player 1"):
            winningCommander = game.p1c
        elif(win=="Player 2"):
            winningCommander = game.p2c
        elif (win=="Player 3"):
            winningCommander = game.p3c
        elif (win=="Player 4"):
            winningCommander = game.p4c
        else:
            continue
        colors[cardColor(winningCommander)] +=1
    return (colors)

# Color identity name given a card object or a list of partners
def cardColor(cmdr):
    if("//" in cmdr):
        part = cmdr.split("//")
        card = scrython.cards.Named(fuzzy=part[0])
        card1 = scrython.cards.Named(fuzzy=part[1])
        identity = card.color_identity() + card1.color_identity()
    else:
        card = scrython.cards.Named(fuzzy=cmdr)
        identity = card.color_identity()
    if('W' in identity and 'U' in identity and 'B' in identity and 'R' in identity and 'G' in identity):
        return "5 color"
    elif('W' in identity and 'U' in identity and 'B' in identity and 'G' in identity):
        return "witch-maw"
    elif ('W' in identity and 'U' in identity and 'R' in identity and 'G' in identity):
        return "ink-treader"
    elif ('W' in identity and 'R' in identity and 'B' in identity and 'G' in identity):
        return "dune-brood"
    elif ('R' in identity and 'U' in identity and 'B' in identity and 'G' in identity):
        return "glint-eye"
    elif ('W' in identity and 'U' in identity and 'B' in identity and 'R' in identity):
        return "yore-tiller"
    elif ('W' in identity and 'U' in identity and 'B' in identity):
        return "esper"
    elif ( 'U' in identity and 'B' in identity and 'R' in identity ):
        return "grixis"
    elif ('B' in identity and 'R' in identity and 'G' in identity):
        return "jund"
    elif ('W' in identity and 'R' in identity and 'G' in identity):
        return "naya"
    elif ('W' in identity and 'U' in identity  and 'G' in identity):
        return "bant"
    elif ('W' in identity and 'B' in identity  and 'G' in identity):
        return "abzan"
    elif ('W' in identity and 'U' in identity and  'R' in identity ):
        return "jeskai"
    elif ( 'U' in identity and 'B' in identity and  'G' in identity):
        return "sultai"
    elif ('W' in identity and 'B' in identity and 'R' in identity):
        return "mardu"
    elif ('U' in identity and 'R' in identity and 'G' in identity):
        return "temur"
    elif ('W' in identity and 'U' in identity):
        return "azorius"
    elif ('U' in identity and 'B' in identity):
        return "dimir"
    elif ('B' in identity and 'R' in identity):
        return "rakdos"
    elif ('R' in identity and 'G' in identity):
        return "gruul"
    elif ('W' in identity and 'G' in identity):
        return "selesnya"
    elif ('W' in identity and 'B' in identity):
        return "orzhov"
    elif ('U' in identity and 'R' in identity ):
        return "izzet"
    elif ('B' in identity and 'G' in identity):
        return "golgari"
    elif ('W' in identity and 'R' in identity):
        return "boros"
    elif ('U' in identity and  'G' in identity):
        return "simic"
    elif('W' in identity):
        return "white"
    elif ('U' in identity):
        return "blue"
    elif ('B' in identity):
        return "black"
    elif ('R' in identity):
        return "red"
    elif ('G' in identity):
        return "green"
    else:
        return "colorless"

# Cmc of commander(s)
def cardCmc(cmdr):
    if ("//" in cmdr):
        part = cmdr.split("//")
        card = scrython.cards.Named(fuzzy=part[0])
        card1 = scrython.cards.Named(fuzzy=part[1])
        if(card.name()!=card1.name()):
            return (float(cardCmc(card.name())) + float(cardCmc(card1.name())))/2
    card = scrython.cards.Named(fuzzy=cmdr)
    cmc = card.cmc()
    cmc = 0 if cmc== "" else float(cmc)
    return cmc

def calcAvgCMC(cmdrs):
    total = 0
    for i in cmdrs:
        total += cardCmc(i)
    return round(total / len(cmdrs),2)

# get list of all players in archive
def getPlayerList():
    p1 = Season2Game.objects.values(pc=F('p1')).distinct()
    p2 = Season2Game.objects.values(pc=F('p2')).distinct()
    p3 = Season2Game.objects.values(pc=F('p3')).distinct()
    p4 = Season2Game.objects.values(pc=F('p4')).distinct()
    combined = list(chain(p1,p2,p3,p4))
    newcombined = []
    for i in combined:
        new = i['pc']
        if(new!="N/A" and new not in newcombined):
            newcombined.append(new)
    newcombined = sorted(newcombined)
    return newcombined

# Player Specific Data

# How many times a player has played a color
def playerColors(played):
    colors = {"colorless": 0, "white": 0, "blue": 0, "black": 0, "red": 0, "green": 0,
              "azorius": 0, "dimir": 0, "rakdos": 0, "gruul": 0, "selesnya": 0, "orzhov": 0, "izzet": 0, "golgari": 0,
              "boros": 0, "simic": 0, "esper": 0, "grixis": 0, "jund": 0, "naya": 0, "bant": 0, "abzan": 0, "jeskai": 0
        , "sultai": 0, "mardu": 0, "temur": 0, "yore-tiller": 0, "glint-eye": 0, "dune-brood": 0, "ink-treader": 0
        , "witch-maw": 0, "5 color": 0}
    for i in played:
        val = int(played[i])
        colors[cardColor(i)] += 1 * val
    return colors

# List of commanders played for a specific person and how many times they played it
def commandersPlayed(player):
    first = Season2Game.objects.filter(p1=player)
    first = first.values(pc =F('p1c'))
    second = Season2Game.objects.filter(p2=player)
    second = second.values(pc=F('p2c'))
    third = Season2Game.objects.filter(p3=player)
    third = third.values(pc=F('p3c'))
    fourth = Season2Game.objects.filter(p4=player)
    fourth = fourth.values(pc=F('p4c'))
    combined = list(chain(first,second,third,fourth))
    thisdict = {}
    for i in combined:
        # exists

        if i['pc'] in thisdict.keys():
            thisdict[i['pc']]+=1
        else:
            thisdict[i['pc']]=1
        # new entry
    return (thisdict)



def dictPieDisplay(name,thisDict, other):
    names1 = list(thisDict.keys())
    values1 = list(thisDict.values())
    total= sum(values1)
    names2 = list(other.keys())
    values2 = list(other.values())
    fig1, (ax1,ax2) = plt.subplots(1,2)
    ax1.pie(values1,labels=names1, explode=None,autopct=lambda p: '{:.0f}%({:.0f})'.format(p,(p/100)*total),shadow=False)
    ax1.set_title("Colors")
    ax2.pie(values2, labels=names2, explode=None, autopct=lambda p: '{:.0f}%({:.0f})'.format(p, (p / 100) * total),shadow=False)
    ax2.set_title("Commanders")
    fig1.canvas.manager.set_window_title("Magic Boi Stats - " + name)
    plt.show()

def display():
    plt.style.use('dark_background')
    combo = colorIdentity()
    names = list(combo.keys())
    values = list(combo.values())
    fig, ax = plt.subplots()
    ax.barh(names,values)
    plt.show()

def CommanderMostPlayedPlayer(cp):
    cp = sorted(cp.items(), key=lambda x:x[1], reverse=True)
    print(cp)
    return scrython.cards.Named(fuzzy=cp[0]).scryfall_uri()

# Remove dictionary items with value of 0
def trimDict(thisdict):
    return {x:y for x,y in thisdict.items() if y!=0}
def main():
    print("Games: " + str(totalGames()))
    print("Turn Order Wins " + str(turnOrderWins()))
    print("Colors Played: " + str(colorIdentity()))
    print("Colors Played Wins: " + str(colorIdentityWins()))
    print(scrython.cards.Named(fuzzy="Valki, god").scryfall_uri())
    allPlayers = getPlayerList()
    for i in allPlayers: # loops through all players
        cp = commandersPlayed(i)
        pc = trimDict(playerColors(cp))
        dictPieDisplay(i,pc,cp)
        print(i)
        print(calcAvgCMC(list(cp.keys())))
        print(CommanderMostPlayedPlayer(cp))

main()