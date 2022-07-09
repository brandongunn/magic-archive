import csv, scrython, time
from homepage.models import Season2Game
def initialLoad():
    with open('./Form Responses - Main.csv', 'r') as file:
        next(file)
        reader = csv.reader(file, skipinitialspace=True)
        cnt = 1
        for row in reader:
            data = Season2Game(gameid = cnt , date=row[1],p1=row[2],p1c=commanderNames(row[3])
                         ,p2=row[4],p2c=commanderNames(row[5]),p3=row[6],p3c=commanderNames(row[7])
                               ,p4=row[8],p4c=commanderNames(row[9])
                         ,winner=row[10])
            data.save()
            cnt+=1
        print("Game Model Has been loaded")

def update():
    with open('./Form Responses - Update.csv', 'r') as file:
        next(file)
        reader = csv.reader(file, skipinitialspace=True)
        cnt = int(Season2Game.objects.latest('gameid').gameid) + 1
        for row in reader:
            data = Season2Game(gameid=cnt, date=row[1], p1=row[2], p1c=commanderNames(row[3])
                               , p2=row[4], p2c=commanderNames(row[5]), p3=row[6], p3c=commanderNames(row[7])
                               , p4=row[8], p4c=commanderNames(row[9])
                               , winner=row[10])
            data.save()
            cnt += 1
        print("Game Model Has been updated")


def commanderNames(cmdrs):
    if(cmdrs == "N/A"):
        return cmdrs
    # partner commanders
    if("//" in cmdrs):
        part = cmdrs.split("//")
        return commanderNames(part[0]) + " // " + commanderNames(part[1])
    # single card commanders
    else:
        try:
            time.sleep(.05)
            card = scrython.cards.Named(fuzzy=cmdrs)
            print("Valid " + card.name() )
            return card.name()
        except Exception:
            vaild = False
            while(not vaild):
                time.sleep(.05)
                auto = scrython.cards.Autocomplete(q=cmdrs, query=cmdrs)
                print(cmdrs + "? Did you mean?")
                for item in auto.data():
                    print(item)
                cmdrs = input("("+cmdrs+") Enter the correct Commander: ")
                return commanderNames(cmdrs)


def main():
    type =input("Is this an update (y/n)")
    if(type == "y"):
        update()
    else:
        initialLoad()

main()