from homepage.models import Season1Game, commanders, comPlayed
import scrython
from collections import OrderedDict
def initialLoad():
    all = Season1Game.objects.all()
    for g in all:
        play1,play2,play3,play4,play5 = g.p1, g.p2, g.p3, g.p4, g.p5
        com1,com2,com3,com4,com5 = g.p1c, g.p2c, g.p3c, g.p4c, g.p5c
        com=[]
        com.append(com1)
        com.append(com2)
        com.append(com3)
        com.append(com4)
        com.append(com5)
        print(com)
        for i in com:
            if i =="N/A":
                continue
            if "||" in i:
                part = i.split("||")
                partners=[]
                print(part)
                partner1 = scrython.cards.Named(fuzzy= part[0])
                partner2= scrython.cards.Named(fuzzy= part[1])
                partners.append(partner1)
                partners.append(partner2)
                try:
                    commanders.objects.get(cname=i)
                except:
                    clr=""
                    temp=[]
                    for k in partners:
                        for r in k.color_identity():
                            r.replace("{", "")
                            r.replace("}", "")
                            clr=clr+r
                            print(clr)
                        temp[:0]=clr
                        clr=""
                        for o in temp:
                            if o in clr:
                                pass
                            else:
                                clr=clr+o


                    b = commanders(cname=i, cmc=partner1.cmc(), color_identity=clr, power=partner1.power(),
                                   toughness=partner1.toughness(), typeLine=partner1.type_line())
                    b.save()
                    print(b)

                continue
            card = scrython.cards.Named(fuzzy=i)
            try:
                #print("try "+i)
                commanders.objects.get(cname=card.name())
            except:
                #print(card.name())
                clr = ""
                for r in card.color_identity():
                    r.replace("{", "")
                    r.replace("}", "")
                    clr = clr + r
                #print(clr)
                if "//" in card.name():
                    #print(card.cmc())
                    tempCmc=card.cmc()
                    fullname= card.name()
                    front = card.card_faces()[0]
                    #print(front)
                    back = card.card_faces()[1]
                    #print(back)

                    if "Creature" in front['type_line'] and "Creature" in back['type_line']:
                        b = commanders(cname=card.name(),cmc=tempCmc,color_identity=clr,power=front['power'],toughness=front['toughness'],typeLine=front['type_line'])
                        b.save()
                        print(front['name']+" Creature Creature")
                    elif "Creature" in front['type_line'] and "Planeswalker" in back['type_line']:
                        b = commanders(cname=card.name(),cmc=tempCmc,color_identity=clr,loyalty=back['loyalty'],power=front['power'],toughness=front['toughness'],typeLine=front['type_line'])
                        b.save()
                        print(front['name']+" Creature Planeswalker")
                    else:
                        b = commanders(cname=card.name(), cmc=tempCmc, color_identity=clr, power=front['power'],
                                       toughness=front['toughness'], typeLine=front['type_line'])
                        b.save()
                        print(front['name'] + " Creature Something")

                    continue
                try:
                    type = card.type_line()
                    type.index("Creature")
                    b = commanders(cname=card.name(),cmc=card.cmc(),color_identity=clr,power=card.power(),toughness=card.toughness(),typeLine=card.type_line())
                    b.save()
                    #print(b)
                except:
                    b = commanders(cname=card.name(),cmc=card.cmc(),color_identity=clr,loyalty=card.loyalty(),typeLine=card.type_line())
                    b.save()
                    #print(b)

def main():
    initialLoad()

main()