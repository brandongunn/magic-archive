from homepage.models import Season1Game,players
from itertools import chain
def initialLoad():
    all_games = Season1Game.objects.all()
    for row in all_games:
        player1 = row.p1.strip()
        player2 = row.p2.strip()
        player3 = row.p3.strip()
        player4 = row.p4.strip()
        player5 = row.p5.strip()
        p=[]
        p.append(player1)
        p.append(player2)
        p.append(player3)
        p.append(player4)
        p.append(player5)
        for i in p:
            try:
                pt = players.objects.get(pname=i)
            except:
                if (i!="N/A"):
                    p1_query = games.objects.filter(p1=i)
                    p2_query = games.objects.filter(p2=i)
                    p3_query = games.objects.filter(p3=i)
                    p4_query = games.objects.filter(p4=i)
                    p5_query = games.objects.filter(p5=i)
                    p1_query = list(chain(p1_query,p2_query,p3_query,p4_query,p5_query))
                    num_wins=0
                    num_losses=0
                    num_draws=0
                    for j in p1_query:
                        tie= j.winner[0:4]
                        tie_people = j.winner[6:]
                        tie_names = tie_people.split(",")
                        if(j.winner.strip()==i):
                            num_wins+=1
                        elif(tie=="Draw"):
                            for k in tie_names:
                                if (k.strip()==i):
                                    num_draws+=1
                                else:
                                    num_losses+=1
                        else:
                            num_losses+=1

                    b = players(pname=i,wins=num_wins,losses=num_losses,draws=num_draws)
                    b.save()


