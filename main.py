from sys import exit

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

class inventory:
    hairpin=False
    money=False
    butterknife=False
    orange=False
    diamond=False
    sword=False
    butter=False
    elfID=False
    cc=False
    fertilizer=False
    keys=False
    cabbage=False
    heart=False


class event:
    feed=False
    cabbages=False
    killsanta=False
    savebabies=False
    gmission=False

def check():
    print('You have: ')
    if inventory.hairpin==True:
        print('hairpin ')
        pass
    if inventory. money==True:
        print('paper ')
        pass
    if inventory.butterknife==True:
        print('butterknife ')
    if inventory.orange==True:
        print('orange' )
    if inventory.butter==True:
        print('butter ')
    if inventory.elfID==True:
        print('elfID ')
    if inventory.cc==True:
        print('candy cane ')
    if inventory.fertilizer==True:
        print('smelly mud ')
    if inventory.diamond==True:
        print('shiny rock ')
    if inventory.sword==True:
        print('sword ')
    if inventory.keys==True:
        print('keys ')
    if inventory.cabbage==True:
        print('cabbage patch kid! ')
    if inventory.heart==True:
        print('battery ')
    else:
        pass


def futurealley():
    print("--------------------------------------------")
    print("You find yourself surrounded by a heap of trash bags in a filthy, deserted alleyway.Your time machine is here, but you cannot return home since it is out of power. Maybe you can 'use' something to power it?"+"\n")
    print("Or you can go 'dumpster diving', 'to main street' or 'climb fire escape'?"+"\n")
    print("Type 'check' to see your inventory at any point in the game"+"\n")
    print("Type 'exit' to quit (no saving!) at any point in the game"+"\n")
    while True:
        blah=input('>>').strip().lower()
        if blah=='dumpster diving':
            dumpster()
        elif blah=='to main street':
            mainst()
        elif blah=='climb fire escape':
            fireesc()
        elif blah=='use battery' and inventory.heart==True:
            print("you powered your time machine with the cabbage heart. ready for takeoff, congratulations!")
            print('END')
            exit()
        elif blah=='check':
            check()
        elif blah == 'exit':
            exit()
        else:
            print('Print something real')


def dumpster():
    print("--------------------------------------------")
    print("You climb into a dumpster and find that you have landed in another pile of garbage. You see the following:'old newspaper','hairpin','butter knife','orange','rock','paper','scissors'")
    print("You can try to 'take' or 'look' at an item or type 'back' to go back to alley."+"\n")
    while True:
        b=input('>>').strip().lower()
        if b=='look old newspaper':
            print('The date is December 26, 3012. Headlines: OH SNaP!'+'\n')
        elif b=='take hairpin':
            print('got it'+'\n')
            inventory.hairpin=True
        elif b=='take butter knife':
            if inventory.butter==False:
                print("there isn't any butter in this game...i'll just leave it."+'\n')
            else:
                print('ok i lied, you can have it')
                inventory.butterknife=True
        elif b=='take orange':
            print("wow not moldy!"+'\n')
            inventory.orange=True
        elif b=='take rock':
            print('ooh a shiny rock. better keep it safe'+'\n')
            inventory.diamond=True
        elif b=='take paper':
            print("some weird markings on a bit of paper, maybe it'll come in handy"+'\n')
            inventory.money=True
        elif b=='take scissors':
            print('ouch. you cut yourself. better not go running around with those.'+'\n')
        elif b=='check':
            check()
        elif b=='back':
            futurealley()
        elif b == 'exit':
            exit()
        else:
            print('type something real'+'\n')


def mainst():
    print("--------------------------------------------")
    print("You see a crowd of people lined up outside 'Santa's Workshop'. A little girl is sleeping in her stroller.")
    print("go to 'alley' or 'talk' to her mom"+'\n')
    while True:
        b=input('>>').strip().lower()
        if b=='talk':
            if event.killsanta==False and event.savebabies==False and event.cabbages==True:
                print('why are you back? HURRY UP AND GET ME SOME CABBAGES')
            if inventory.cabbage==True:
                print('Is that what I think it is? How did you get this? Now we can finally go home and celebrate the holidays.')
                print("Take this cabbage patch heart.It's a very strong 'battery', we won't need it and you might need it for your travels...in time"+'\n')
                inventory.heart=True
                futurealley()
            elif event.feed==False:
                print("--------------------------------------------")
                print("Help stranger! My daughter hasn't eaten in days, but we can't leave or else we won't be first in line when Santa's Workshop opens."+'\n')
                print("'use' something to help her")
                o=input('>>').strip().lower()
                if inventory.orange==True and o=='use orange':
                    event.feed=True
                    inventory.orange=False
                    print("--------------------------------------------")
                    print('Thank you so much!'+'\n')
                    mainst()
                else:
                    print("that's not food. thanks for nothing"+'\n')
                    mainst()
            elif event.feed==True and event.cabbages==False:
                print("--------------------------------------------")
                print("We have been waiting here for days to purchase the new cabbage patch kids in time for Christmas...but Santa has been naughty this year, and didn't produce them on time")
                print("I need you to get me a cabbage patch kid as soon as possible, or else my daughter might die from exhaustion if we wait here much longer"+'\n')
                print("The elves have barred the front doors. You'll have to find another way in."+'\n')
                event.cabbages=True
                mainst()
        elif b=='alley':
            futurealley()
        elif b=='check':
            check()
        elif b=='exit':
            print('byebyebye')
            exit()
        else:
            print('print something real'+'\n')

def fireesc():
    print("You are on the fire escape.")
    print("climb to level 'two','three' or 'roof'? Or go back to 'alley'"+'\n')
    while True:
        x=input('>>').strip().lower()
        if x=='two':
            secfloor()
        elif x=='three':
            thirfloor()
        elif x=='roof':
            roof()
        elif x=='alley':
            futurealley()
        elif x=='check':
            check()
        elif x=='exit':
            print('goodbye')
            exit()
        else:
            print('print something real')

def secfloor():
    print('you see a locked window. inside there appears to be a greenhouse, with rows upon rows of sleeping cabbages.')
    print("do you want to 'break window' to get into the factory. or go to 'another level'?"+'\n')
    while True:
        pie=input('>>').strip().lower()
        if pie=='another level':
            fireesc()
        elif pie=='use hairpin':
            print('you use your ninja skills to quietly unlock the window'+'\n')
            factory()
        elif pie=='break window':
            print("you bust in there like nobody's business. unfortunately there is an ALARM")
            print("you are captured by reindeerbots"+'\n')
            dungeon()
        elif pie=='check':
            check()
        elif pie=='exit':
            print('farewell loser.')
            exit()
        else:
            print('print something real')


def dungeon():
    count=0
    print("you are in a dungeon. one elf guards your cell. 'talk' or 'look'"+'\n')
    while True:
        d=input('>>').strip().lower()
        if d=='look':
            print("there's a toilet, and a chair. that's it.")#prints else statement when looking after talking
        if d=='talk':
            if event.cabbages==True and inventory.elfID==False:
                if count<2:
                    count=count+1
                    print("Quiet. I know what you're here for, and there's no way I'm helping you out. You're gonna rot in here for the rest of eternity."+'\n')
                else:
                    print("you're so annoying. how can i even tell you're trustworthy? 'give' me something of value and I will tell you what you need to know")
                    s=input('>>').strip().lower()
                    if s=='give rock'and inventory.diamond==True:
                        print("precious diamonds...ok here's the deal. Santa's a fraud. he's been harvesting energy from the cabbage patch kids for years to power his personal tanning bed.then when they're all withered and dead, he sprays them with drugs and sells them to little kids to raise a fund to build bigger, more expensive tanning beds! only you can stop him, by defeating santa, and using his keys to turn off the generator and save the cabbage patch kids"+'\n')
                        print("i'll let you go for now.here's an 'elfID' to help you in your mission. next time use ******* to unlock the window, or else you'll wind up here again! :D"+'\n')
                        inventory.elfID=True
                        inventory.diamond=False
                        futurealley()
                    else:
                        print("that's garbage. your time is up anyway, so get out"+'\n')
                        futurealley()
            else:
                if count<2:
                    count=count+1
                    print("commit the crime, do the time. you're lucky we don't deport you back to whatever planet you came from scum ;)"+'\n')
                else:
                    print("time's up.you have no more business here.")
                    futurealley()
        if d=='check':
            print("dunno why you're just wasting time here, but ")
            check()
        elif d=='exit':
            print('QUITTER')
            exit()
        else:
            print("you're stuck")


def factory():
    print("here is the 'cabbage patch'. an elf is pruning the patch.you see a 'fridge'. you can 'inpect' something, 'talk' or take 'stairs' to another level")
    print("type 'back' to go back to the fire escape")
    while True:
        moo=input('>>').strip().lower()
        if moo=='check':
            check()
        if moo=='inspect fridge':
            print("jk. there's a plate of 'butter'")
            print("'take' it? (y/n)")
            x=input('>>').strip().lower()
            if x=='y':
                inventory.butter=True
                print("got'emm"+'\n')
                factory()
            else:
                print("not everyone likes butter."+'\n')
                factory()
        elif moo=='inspect cabbage patch':
            print("The leafy green babies are snoozing away peacefully in their soilbeds. Your heart almost breaks after witnessing their cuteness."+'\n' "Maybe you should try to 'take cabbage'?")
        elif moo=='take cabbage':
            if event.gmission==False:
                print("ZAP. the cabbage patch kid shocked you when you tried to grab it! you see they are all connected with a maze of wires."+'\n')
            else:
                print("You rip a few squalling cabbage patch kids up and stuff them in your jacket. the perfect present for a tired little girl!")
                inventory.cabbage=True
                event.savebabies=True
        elif moo=='talk':
            print("eyeyey. you're not supposed to be in here! Unless... can you help me out?")
            print("I need some 'fertilizer' for the cabbage babies. 'give' me some and I'll tell you a secret."+'\n')
            dots=input('>>').strip().lower()
            if dots=='give fertilizer' and inventory.fertilizer==True:
                print("ah perfect! now here's the secret: Santa's weakness is buttered candy canes, and you can only make them in his room on the third floor."+'\n')
                factory()
            else:
                print("that's not fertilizer")
                factory()
        elif moo=='stairs':
            print("GENERATOR ROOM. enter the password to enter. Hint:it's elemental, my dear"+'\n')
            x=input('>>').strip().lower()
            if x=='oxygenhydrogensulfursodiumphosphorus':
                groom()
            else:
                print('sorry bud. no spaces next time.')
                factory()
        elif moo=='back':
            fireesc()
        elif moo=='exit':
            exit()
        else:
            print('printsomethingreal')


def thirfloor():
    print(" You've reached a balconey. An elf is cleaning 'muddy tracks' off the floor and the doors are locked, but maybe you could 'swipe' a card to unlock it.")
    print("'inspect' something or 'talk' or go to 'another level'?"+'\n')
    while True:
        d=input('>>').strip().lower()
        if d=='check':
            check()
        if d=='another level':
            fireesc()
        if d=='swipe elfid':
            santaroom()
        if d=='inspect muddy tracks':
            print("actually that's not mud... take some? (y/n)"+'\n')#prints else statement when looking after talking
            x=input('>>').strip().lower()
            if x=='y':
                inventory.fertilizer=True
                print("got'emm")
                thirfloor()
            else:
                print("alright,alright...no need to be a pansy about it."+'\n')
                thirfloor()
        if d=='talk':
            print("hey. hey you. can i let you in on a little secret? but only if you 'give' me what i want first."+'\n')
            x=input('>>').strip().lower()
            if x=='give paper':
                inventory.cc=True
                inventory.money=False
                print("hehe. i love the smell of money in the morning. here are some good candy canes. use them wisely. oh and my secret? santa reads the newspaper. and loves the periodic table."+'\n')
                thirfloor()
            else:
                print("you gotta pay to play man"+'\n')
                thirfloor()
        elif d=='exit':
            print('QUITTER')
            exit()
        else:
            print("print something real")


def santaroom():
    print("From the huge bed, fuzzy red sheets and carpet, you can tell this is santa's bedroom")
    if inventory.butter==True and inventory.cc==True and inventory.butterknife==True:
        print("you feel a sense of purpose as you look at your inventory. combine items? (y/y)")
        while True:
            x=input('>>').strip().lower()
            if x=='y':
                print("you have made 'buttered candy cane sword' it's pretty slippery. now begone!")
                inventory.sword=True
                inventory.butter=False
                inventory.cc==False
                inventory.butterknife==False
                thirfloor()
            else:
                print("alright, this is the only thing that's going to save you sucker. now leave.")
                thirfloor()
    else:
        print("you aren't ready for the epicness of this room.")
        print("you stumble around some more, and... fall into a trap!"+'\n')
        dungeon()


def roof():
    print("you see a huge red something sleeping in what looks to be an even bigger white coffin. 'poke'? or go 'back'?")
    while True:
        x=input('>>').strip().lower()
        if x=='check':
            check()
        if x=='poke':
            if event.killsanta==True:
                print( "what are you doing? he's already dead, now get out of here.")
                fireesc()
            if inventory.sword==True and event.killsanta==False:
                print("omfg you killed santa. steal his keys? (y/n)")
                event.killsanta=True
                y=input('>>').strip().lower()
                if y=='y':
                    inventory.keys=True
                    fireesc()
                else:
                    print('too bad, lives are at stake here and you rip the keys off his lifeless body')
                    inventory.keys=True
                    fireesc()
            else:
                print("you're not ready yet, my young padawan")
        elif x=='back':
            fireesc()
        elif x=='exit':
            exit()
        else:
            print('type something real')


def groom():
    print("you made it! this is the generator room. 'use keys' to turn off the machine. or type 'back' to go to the factory")
    while True:
        x=input('>>').strip().lower()
        if x=='check':
            check()
        if x=='use keys' and inventory.keys==True:
            print('the power went out. now you can take a cabbage patch kid.')
            event.gmission=True
            inventory.keys==False
        elif x=='use keys' and inventory.keys==False:
            print('what keys?')
        elif x== 'back':
            factory()
        elif x=='exit':
            exit()
        else:
            print('type something real')




futurealley()
