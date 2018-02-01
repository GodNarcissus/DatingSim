import random
#allows for speech checks and randomly occuring events
import time
#allows for the text to not all show up at once

class Character(object):
    def __init__(self,name,location):
        self.name = name
        self.location = location
#gives all npc's and the player the same class. each character will have a name & a place they'll reside.

heart = []
#the home of major depression if the player hates themself

greetings = ["hi", "hey", "yo", "what's up", "hello", "hola", "what's good"]
#list of ways the player can greet someone

map = {"tutorial" : "Tutorial"}
#will represent the player's accessable areas

discovered = ["tutorial"]
#will represent the player's visited locations

enemies = []
#will represent list of those you've upset

acquaintances = []
#will represent the people the player has already talked to

friends = []
#will represent the people the player has become friends with

inventory = {"dollars" : 0}
#will represent the player's wallet

myself = Character("x","tutorial")
#this is the player!

colette = Character("Colette","tutorial")
#this is the tutorial lady

abby = Character("Abby","joecollinspark")
#this is the skater girl

paul = Character("Paul","joecollinspark")
#this is the volleyball character

shane = Character("Shane","dairyqueen")
#this is the cashier at DQ

jeremy = Character("Jeremy", myself.location)
#this is your Uber driver, the person who will transport you to different locations

simi = Character("Simi", myself.location)
#this is the siri equivalent/narrator

#basically what the player can do in any location after the tutorial
def options():
    a = input('\x1b[0;30;47m>>>\x1b[0m ').lower()
    for x in greetings:
        if a == f"{x} simi":
            talkto(simi)
            #opens phone
        elif a == f"{x} myself" or a == f"{x} me" or a == f"{x} {myself.name}":
            talkto(myself)
            #talk to yourself
        elif a == f"{x} jeremy":
            talkto(jeremy)
        elif a == f"{x} colette":
            talkto(colette)
            #talk to tutorial lady
        elif a == f"{x} abby":
            talkto(abby)
            #talks to the skater
        elif a == f"{x} paul":
            talkto(paul)
            #talks to volleyball player
        elif a == f"{x} shane":
            talkto(shane)
            #talks to the cashier
    if a == "call uber" or a == "call uber driver":
        call_uber()
        #can travel to different locations
    elif a == "wallet":
        wallet()
        #pulls up a dictionary of how much money you have
    elif a == "map":
        gps()
        #can see the list of available locations
    elif a == "contacts":
        contacts()
        #can see friends list
    elif a == "look around":
        observe()
        #gives a description of the area
    elif a == "call uber" or a == "call uber driver":
        call_uber()
        #talks to Uber driver
    elif a == "go to tennis court":
        approach("tennis court")
        #learns the skater's name
    elif a == "go to volleyball net":
        approach("volleyball net")
        #learns the volleyball player's name
    elif a == "go to cash register":
        approach("cash register")
        #learns the cashier's name

#will show what's in the player's inventory
def wallet():
    for key, value in inventory.items():
        print(f"{key} -- {value}")

def gps():
    print("|", end=" ")
    for x in map:
        print(map[x], end=" | ")
    print('\x1b[1;37;40m' + "MAP" + '\x1b[0m')
        #gives a list of locations on the same line
        #anything with '\x1b...' changes the color of the text to differentiate different character dialogues

def discover():
    discovered.append(myself.location)
    #adds a visited location to list of discovered places. opens introductory dialogue to the place if not discovered

def contacts():
    print("|", end=" ")
    for x in friends:
        print(x.name, end=" | ")
    print('\x1b[1;37;40m' + "CONTACTS" + '\x1b[0m')
        #gives a list of friends' names on the same line

#function for changing the player's location
def call_uber():
    print("calling your Uber driver...")
    time.sleep(2)
    if jeremy in acquaintances:
        print('\x1b[0;30;47m' + f"What's up, {myself.name}? Where you wanna go?" + '\x1b[0m')
        time.sleep(s)
        print('\x1b[0;30;47m' + "Just tell me where." + '\x1b[0m')
    elif jeremy in friends:
        print('\x1b[0;30;47m' + f"What's up, {myself.name}? Where you wanna go?" + '\x1b[0m')
        time.sleep(s)
        print('\x1b[0;30;47m' + "I'll take you anywhere you need." + '\x1b[0m')
    elif jeremy in enemies:
        print('\x1b[0;30;47m' + "Oh it's you." + '\x1b[0m')
        time.sleep(s)
        print('\x1b[0;30;47m' + "Let's get this over with." + '\x1b[0m')
    else:
        print('\x1b[0;30;47m' + "What's up? I'm Jeremy, your Uber driver." + '\x1b[0m')
        time.sleep(s)
        print('\x1b[0;30;47m' + "Where you wanna go?" + '\x1b[0m')
    time.sleep(s)
    while True:
        gps()
        #shows the list of locations the player can travel to
        d = input(">>> ").lower().replace(" ", "")
        if d == myself.location.lower().replace(" ", ""):
            #prevents user from "moving" to the same location. also makes it so in the beginning you're forced to leave tutorial
            print('\x1b[0;30;47m' + "My dude we're already here!" + '\x1b[0m')
            time.sleep(s)
            print('\x1b[0;30;47m' + "Don't make me waste my time!" + '\x1b[0m')
        elif d in map:
            print('\x1b[0;30;47m' + "Going there now, my dude." + '\x1b[0m')
            time.sleep(1)
            print("traveling...")
            time.sleep(1)
            #the player, Uber driver, and phone/narrator all travel together
            myself.location=d
            jeremy.location=d
            simi.location=d
            print('\x1b[0;30;47m' + "Aight we here now. I'll be waiting here if you need me." + '\x1b[0m')
            time.sleep(1)
            print(f"you are now at {map[d]}.")
            if "joecollinspark" not in discovered:
                #automatic encounter directly after tutorial
                print("by the way, I'm Simi, the AI in your phone.")
                time.sleep(s)
                print("i normally reside in the Tutorial, but Colette put me in your phone so I could tag along.")
                time.sleep(s)
                print("think of me as the narrator, I'll always be with you.")
                time.sleep(s)
                print("if you have any questions, want to see all the apps on your phone, or just want to talk")
                time.sleep(s)
                print("just say, \x1b[3;37;40mhey simi\x1b[0m.")
                time.sleep(s)
                print("if you're not sure what to do, you can always look around or talk to me for help.")
                time.sleep(s)
                print("you're in free roam mode now, indicated by the inversed colored \x1b[3;37;40m>>>\x1b[0m.")
                discover()
            elif myself.location not in discovered:
                #keeps track of visited areas and prevents automatic encounters from happening again
                discover()
            break
        else:
            #makes sure the player types in a valid location on their map
            print('\x1b[0;30;47m' + "I can't find that location in my gps." + '\x1b[0m')
            time.sleep(s)
            print('\x1b[0;30;47m' + "Make sure you tell me the location exactly as it is on your map. Copy & paste it if you need to." + '\x1b[0m')

#gives a description of the place the player is in
def observe():
    if myself.location == "joecollinspark":
        print("the park is plenty busy today.")
        time.sleep(s)
        print("however, two people specifically catch your attention.")
        time.sleep(s)
        print("in the \x1b[4;37;40mtennis court\x1b[0m, instead of playing tennis, there's a girl skateboarding.")
        time.sleep(s)
        print("she seems to be struggling learning how to ollie.")
        time.sleep(s)
        print("behind the fenced court, you see someone has set up a \x1b[4;37;40mvolleyball net\x1b[0m.")
        time.sleep(s)
        print("he looks like he's practicing a jumping serve.")
    elif myself.location == "tutorial":
        print("the room is well lit by hanging lightbulbs in the shape of wolf heads from the ceiling.")
        time.sleep(s)
        print("Colette has an interesting taste in decorations.")
    elif myself.location == "dairyqueen":
        print("the store is surprisingly empty.")
        time.sleep(s)
        print("the only person inside is a girl at the \x1b[4;37;40mcash register\x1b[0m.")
    time.sleep(s)

def win():
    print("nice job! you've become friends with everyone in the game!")
    time.sleep(s)
    print("you can now call yourself an expert at making friends,")
    time.sleep(s)
    print("certified by this friendship simulator!")
    while True:
        a = input(">>> ")
        if a == "help":
            print("you've won!")

#will be called when the player is depressed
def dead():
    while "major depression" in heart:
        a = input(">>> ").lower()
        if a == "i am god":
            print("oh yeah that's right, you can never feel depressed.")
            time.sleep(s)
            print("my bad.")
            time.sleep(s)
            print("you are now happy again (I guess?).")
            #secret code that lets you come back to life and overcome depression
            heart.remove("major depression")
            break
        else:
            k = random.randint(1,2)
            if k == 1:
                print("you are way too sad to talk to anyone.")
            else:
                print("if only there was something you could say to yourself to boost your confidence.")

def apologize(character):
    if character == colette:
        #if the player wants colette to forgive them, gives a different speech tree
        while True:
            #if speech check is passed, player can be friends with Colette and get closer to completing the game
            r = input("""\x1b[1;37;40mColette is still crying in the corner, what do you say?\x1b[0m
    \x1b[1;31;40m1. Hey Colette, I'm really sorry.\x1b[0m
    2. Yeah, I don't care anymore. I'm out.

>>> """)
            if r == "1":
                print("Hey Colette, I'm really sorry.")
                time.sleep(s)
                k=random.randint(1,4)
                if "self confidence" in inventory:
                    k = 1
                if k == 1:
                    print('\x1b[5;35;40m' + "Okay, I forgive you, you sound genuine." + '\x1b[0m')
                    enemies.remove(colette)
                    break
                else:
                    print('\x1b[5;35;40m' + "No! Go away! Don't talk to me!" + '\x1b[0m')
                    time.sleep(s)
                    print("\x1b[1;37;40mmaybe you should try again.\x1b[0m")
            elif r == "2":
                print("Yeah, I don't care anymore. I'm out.")
                break
            else:
                print("\x1b[1;37;40mwhat will you do?\x1b[0m")
        if colette not in enemies:
            print('\x1b[5;35;40m' + "Hey, since we're friends now, why don't I give you my number." + '\x1b[0m')
            time.sleep(s)
            print("\x1b[1;37;40mColette is now your friend!\x1b[0m")
            friends.append(colette)

#introduction dialogues, after going to where a person is, this will tell the player their names so they can talk to the characters
def approach(place):
    print('\x1b[1;37;40m' + f"Hi, I'm {myself.name}." + '\x1b[0m')
    time.sleep(s)
    if place == "corner":
        if myself.location == "tutorial":
            print('\x1b[5;35;40m' + f"Hi! My name is Colette." + '\x1b[0m')
        else:
            print("you can't go there from here.")
    elif place == "tennis court":
        if myself.location == "joecollinspark":
            print('\x1b[5;31;40m' + "Uh, hi. I'm Abby." + '\x1b[0m')
        else:
            print("you can't go there from here.")
    elif place == "volleyball net":
        if myself.location == "joecollinspark":
            print('\x1b[5;32;40m' + "Hey, I'm Paul." + '\x1b[0m')
        else:
            print("you can't go there from here.")
    elif place == "cash register":
        if myself.location == "dairyqueen":
            print('\x1b[5;33;40m' + "Hi, I'm Shane." + '\x1b[0m')
        else:
            print("you can't go there from here.")



def talkto(character):
#the talkto() function allows for the player to interact with the npc's
    if myself.location == character.location:
        print('\x1b[1;37;40m' + f"Hey {character.name}!" + '\x1b[0m')
        time.sleep(s)
        #begins speech tree with DQ cashier
        if character == shane:
            if shane in friends:
                while True:
                    r = input(f"""\x1b[5;33;40mHi, {myself.name}! What can I get you?\x1b[0m
    1. Can I get a 5 Buck Lunch?
    2. Nothing.

>>> """)
                    if r == "1":
                        if inventory["dollars"] == 5:
                            print("\x1b[1;37;40mCan I get a 5 Buck Lunch?\x1b[0m")
                            time.sleep(s)
                            print("you give Shane the $5")
                            inventory["dollars"] -= 5
                            time.sleep(s)
                            print("you now have a 5 buck lunch.")
                            inventory["5 buck lunch"] = 1
                            time.sleep(s)
                            print("\x1b[5;33;40mHave a nice day!\x1b[0m")
                            break
                        else:
                            print("\x1b[5;33;40mI'm sorry, but you don't have enough money.\x1b[0m")
                            break
                    elif r == "2":
                        print("\x1b[1;37;40mNothing.\x1b[0m")
                        time.sleep(s)
                        print("\x1b[5;33;40mOkay, have a nice day!\x1b[0m")
                        break
                    else:
                        print("\x1b[5;33;40mI'm sorry, I didn't catch that.\x1b[0m")
            else:
                while True:
                    r = input("""\x1b[5;33;40mHi, welcome to Dairy Queen. What can I get you?\x1b[0m
    1. Can I get a 5 Buck Lunch?
    \x1b[1;32;40m2. Can I have your friendship?\x1b[0m
    3. Nothing.

>>> """)
                    if r == "1":
                        if inventory["dollars"] == 5:
                            print("\x1b[1;37;40mCan I get a 5 Buck Lunch?\x1b[0m")
                            time.sleep(s)
                            print("you give Shane the $5")
                            inventory["dollars"] -= 5
                            time.sleep(s)
                            print("you now have a 5 buck lunch.")
                            inventory["5 buck lunch"] = 1
                            time.sleep(s)
                            print("\x1b[5;33;40mHave a nice day!\x1b[0m")
                            break
                        else:
                            print("\x1b[5;33;40mI'm sorry, but you don't have enough money.\x1b[0m")
                            break
                    elif r == "2":
                        print('\x1b[1;37;40m' + "Can I have your friendship?" + '\x1b[0m')
                        time.sleep(s)
                        k=random.randint(1,4)
                        if "self confidence" in inventory:
                            k = 2
                        if k == 1:
                            print("\x1b[5;33;40mHaha no, sorry.\x1b[0m")
                            break
                        else:
                            print("\x1b[5;33;40mSure; working here is pretty boring.\x1b[0m")
                            time.sleep(s)
                            print("Shane is now your friend!")
                            friends.append(shane)
                            break
                    elif r == "3":
                        print("\x1b[1;37;40mNothing.\x1b[0m")
                        time.sleep(s)
                        print("\x1b[5;33;40mOkay, have a nice day!\x1b[0m")
                        break
                    else:
                        print("\x1b[5;33;40mI'm sorry, I didn't catch that.\x1b[0m")
        #begins speech tree with Uber driver
        elif character == jeremy:
            if jeremy in friends:
                print('\x1b[0;30;47m' + "Whaddup dude." + '\x1b[0m')
            else:
                while True:
                    r = input(f"""\x1b[0;30;47mWhat's good, {myself.name}?\x1b[0m
    1. Just chilling wbu.
    2. I'm tryna make friends.
    3. Nevermind.

>>> """)
                    if r == "1":
                        print("\x1b[1;37;40mJust chilling wbu.\x1b[0m")
                        time.sleep(s)
                        print("\x1b[0;30;47mSweeet.\x1b[0m")
                        time.sleep(s)
                        print("\x1b[0;30;47mTake my number if you wanna chill outside of Uber rides.\x1b[0m")
                        time.sleep(s)
                        print("Jeremy is now your friend!")
                        friends.append(jeremy)
                        break
                    elif r == "2":
                        print("\x1b[1;37;40mI'm tryna make friends.\x1b[0m")
                        time.sleep(s)
                        print("\x1b[0;30;47mSweeet.\x1b[0m")
                        time.sleep(s)
                        print("\x1b[0;30;47mGood luck with that.\x1b[0m")
                        break
                    elif r == "3":
                        print("\x1b[1;37;40mNevermind.\x1b[0m")
                        time.sleep(s)
                        print("\x1b[0;30;47mDon't waste my time.\x1b[0m")
                        break
                    else:
                        print("\x1b[0;30;47mI don't know what you're saying.\x1b[0m")
        #begins talking to yourself
        elif character == myself:
            if myself in friends:
                time.sleep(s)
                print('\x1b[1;37;40m' + "Stop talking to yourself and make some actual friends!" + '\x1b[0m')
            else:
                while True:
                    time.sleep(s)
                    r = input("""\x1b[1;37;40mHey me!\x1b[0m
    1. You are an amazing person.
    2. Kill yourself.
    3. Goodbye.

>>> """)
                    if r == "1":
                        print("\x1b[1;37;40mYou are an amazing person.\x1b[0m")
                        time.sleep(s)
                        print("\x1b[1;37;40mThank you! You are wonderful too!\x1b[0m")
                        time.sleep(s)
                        print("you now have self confidence!")
                        inventory["self confidence"] = 1
                        friends.append(myself)
                        time.sleep(s)
                        print("you now will pass all speech checks.")
                        break
                    elif r == "2":
                        print("\x1b[1;37;40mKill yourself.\x1b[0m")
                        time.sleep(s)
                        print("\x1b[1;37;40m...\x1b[0m")
                        time.sleep(s)
                        print("\x1b[1;37;40mOkay.\x1b[0m")
                        time.sleep(s)
                        print("you now have major depression.")
                        heart.append("major depression")
                        break
                    elif r == "3":
                        print("\x1b[1;37;40mGoodbye.\x1b[0m")
                        time.sleep(s)
                        print("\x1b[1;37;40mBye!\x1b[0m")
                        break
                    else:
                        print("\x1b[1;37;40mWhat am I even saying?\x1b[0m")
        #begins Colette's speech tree
        elif character == colette:
            if colette in friends:
                #if you choose to go back to the tutorial location and talk to colette, gives a different speech tree
                print('\x1b[5;35;40m' + "Hi friend! How are you?" +'\x1b[0m')
            elif colette in enemies:
                apologize(colette)
            else:
                acquaintances.append(colette)
                #sets it so you've talked to colette
                print('\x1b[5;35;40m' + f"Hello! Good job, your greeting is quite plain but it does the trick just fine." + '\x1b[0m')
                time.sleep(s)
                #the player can respond to a person's question by typing in the number corresponding to their desired answer
                while True:
                    r = input("""\x1b[5;35;40mAnyways, below is a dialogue branch. Type in the number corresponding the response you'd like to give to my statement.\x1b[0m
    1. So, like this, right?
    2. I don't really want to.
    3. I'm not too sure how to do this
    4. I don't need this stupid tutorial. I know how to talk to people.

>>> """)
                    if r == "1":
                        print("So, like this, right?")
                        time.sleep(s)
                        print('\x1b[5;35;40m' + f"Yes! That's perfect, {myself.name}. Easy, right?" + '\x1b[0m')
                        break
                    elif r == "2":
                        print("I don't really want to.")
                        time.sleep(s)
                        print('\x1b[5;35;40m' + "Well even if you didn't, you responded just now." + '\x1b[0m')
                        break
                    elif r == "3":
                        print("I'm not too sure how to do this.")
                        time.sleep(s)
                        print('\x1b[5;35;40m' + "It's alright! You did it just now. Isn't it easy?" + '\x1b[0m')
                        break
                    elif r == "4":
                        #makes colette mad at the player
                        print("I don't need this stupid tutorial. I know how to talk to people.")
                        time.sleep(s)
                        print('\x1b[5;35;40m' + "..." + '\x1b[0m')
                        time.sleep(1)
                        print('\x1b[5;35;40m' + "..." + '\x1b[0m')
                        time.sleep(1)
                        print('\x1b[5;35;40m' + "Fine! If you think you can make friends without my help go on right ahead!" + '\x1b[0m')
                        enemies.append(colette)
                        acquaintances.remove(colette)
                        time.sleep(s)
                        while colette in enemies:
                            r = input("""\x1b[1;37;40mColette storms off and leaves you alone in the Tutorial room. what would you like to do?\x1b[0m
    1. Finally, let's start the game already.
    2. I better go apologize, what I said was wrong.

>>> """)
                            if r == "2":
                                #gives chance to continue tutorial and win back Colette's admiration
                                print("I better go apologize, what I said was wrong.")
                                time.sleep(s)
                                print("\x1b[1;37;40myou chase after Colette to find her sobbing on the floor.\x1b[0m")
                                time.sleep(s)
                                apologize(colette)
                                break
                            elif r == "1":
                                #skips tutorial
                                print('\x1b[1;37;40m' + "Finally, let's start the game already." + '\x1b[0m')
                                break
                            else:
                                print("make a decision.")
                        break
                    else:
                        print('\x1b[5;35;40m' + "Type in one of the given numbers, I can't understand you." +'\x1b[0m')
                    time.sleep(s)

                time.sleep(s)
                while colette not in enemies:
                    #continues conversation as long as player didn't roast colette
                    print("\x1b[5;35;40mBelow is a speech check. The 3 colors represent the success chance you have of passing it.\x1b[0m")
                    time.sleep(s)
                    r = input("""\x1b[5;35;40mHow charismatic do you think you are?\x1b[0m
    \x1b[1;32;40m1. I wouldn't say I'm very charismatic, but I think I can talk just fine.\x1b[0m
    \x1b[1;33;40m2. I'm pretty charismatic, I'd say.\x1b[0m
    \x1b[1;31;40m3. I'm an amazing speaker, I can make friends with no problem.\x1b[0m
    4. I don't know; charisma isn't really my specialty.

>>> """)
                    time.sleep(s)
                    if r == "1":
                        #easiest choices are green
                        print('\x1b[1;37;40m' + "I wouldn't say I'm very charismatic, but I think I can talk just fine." + '\x1b[0m')
                        time.sleep(s)
                        k=random.randint(1,4)
                        #creates a random number
                        if k == 1:
                        #25% chance to get a 1; 25% chance to fail check
                            print('\x1b[5;35;40m' + "Yeah you really are a lousy speaker. Oh well, can't be helped." + '\x1b[0m')
                            time.sleep(s)
                        else:
                        #75% not to get a 1; 75% chance to pass check
                            print('\x1b[5;35;40m' + "Don't be silly; I think you have a lot of charisma!" + '\x1b[0m')
                            time.sleep(s)
                        break
                    elif r == "2":
                        #medium choices are yellow
                        print('\x1b[1;37;40m' + "I'm pretty charismatic, I'd say." + '\x1b[0m')
                        time.sleep(s)
                        k=random.randint(1,2)
                        if k == 1:
                            print('\x1b[5;35;40m' + "Uhh... think again. You might need to work on that." + '\x1b[0m')
                            time.sleep(s)
                        else:
                            print('\x1b[5;35;40m' + "You certainly are! I think you'll be able to make friends pretty easily." + '\x1b[0m')
                            time.sleep(s)
                        break
                    elif r == "3":
                        #hardest choices are red
                        print('\x1b[1;37;40m' + "I'm an amazing speaker, I can make friends with no problem." + '\x1b[0m')
                        time.sleep(s)
                        k=random.randint(1,4)
                        if k == 1:
                            print('\x1b[5;35;40m' + "Wow, I can see where you're coming from. You're pretty confident too." + '\x1b[0m')
                            time.sleep(s)
                        else:
                            print('\x1b[5;35;40m' + "Um, I don't think so. You might need to tone it down a bit." + '\x1b[0m')
                            time.sleep(s)
                        break
                    elif r == "4":
                        #100% choices are the usual white
                        print('\x1b[1;37;40m' + "I don't know; charisma isn't really my specialty." + '\x1b[0m')
                        time.sleep(s)
                        print('\x1b[5;35;40m' + "Some people are a little more shy than others. That's fine." + '\x1b[0m')
                        break
                    else:
                    #prevents user from typing something not fitting
                        print('\x1b[5;35;40m' + "I'm sorry, I don't know what you're trying to say." + '\x1b[0m')
                        time.sleep(s)
                if colette not in enemies:
                    print('\x1b[5;35;40m' + "You've been doing a great job so far!" +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "I only have a couple of quick tips to show you before I send you on your way." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "Here have this cell phone. It has many uses." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "To look at the locations you can visit in the game, check out the map." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "Just say whatever app you want to use, the phone is voice activated." +'\x1b[0m')
                    print("say \x1b[3;37;40mmap\x1b[0m.")
                    while True:
                        #forces player to test map command
                        a=input(">>> ").lower()
                        for x in greetings:
                            if a == f"{x} colette":
                                print('\x1b[5;35;40m' + "Go ahead, look at the map on the phone I just gave you." +'\x1b[0m')
                        if a == "map":
                            gps()
                            break
                    time.sleep(1)
                    print('\x1b[5;35;40m' + "Now, the goal of this game is to make as many friends as possible." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "People will normally give you their number if you're able to befreind them." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "You can see your friends in your contacts list. Try it now." +'\x1b[0m')
                    time.sleep(1)
                    print("say \x1b[3;37;40mcontacts\x1b[0m.")
                    while True:
                        #forces player to test contacts command
                        a=input(">>> ").lower()
                        for x in greetings:
                            if a == f"{x} colette":
                                print('\x1b[5;35;40m' + "Check out your contacts." +'\x1b[0m')
                        if a == "contacts":
                            contacts()
                            break
                    time.sleep(1)
                    print('\x1b[5;35;40m' + "Oh right, I just gave you the phone so you won't have any numbers yet." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "You can have mine then! I'll be your first friend!" +'\x1b[0m')
                    time.sleep(s)
                    print("Colette is now your friend!")
                    friends.append(colette)
                    acquaintances.remove(colette)
                    #adds Colette to friends list and removes her from acquaintances
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "Congratulations! You've finished the tutorial!" +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "I have one final thing to teach you before you leave." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "To travel to different places in your map, call up an Uber." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "Try looking for more friends at the park nearby, 'Joe Collins.'" +'\x1b[0m')
                    time.sleep(s)
                    map["joecollinspark"] = "Joe Collins Park"
                    #player can now travel to Joe Collins Park
                    print("'Joe Collins Park' has been added to your map!")
                    time.sleep(s)
                    print('\x1b[5;35;40m' + f"Goodbye, {myself.name}! I hope you'll be able to make more friends soon!" +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "You can call your Uber now to take a look at the park." +'\x1b[0m')
                    time.sleep(s)
                    print("say \x1b[3;37;40mcall Uber\x1b[0m.")
                    while True:
                        #forces player to leave and call an Uber
                        a=input(">>> ").lower()
                        for x in greetings:
                            if a == f"{x} colette":
                                print('\x1b[5;35;40m' + "Call your Uber now." +'\x1b[0m')
                        if a == "call uber" or a == "call uber driver":
                            call_uber()
                            break
        elif character == simi:
            while True:
                time.sleep(1)
                a = input(f"""hi {myself.name}, what do you need?
    1. What are some of the commands or apps I can say?
    2. I just wanted to talk to you.
    3. I need some help.
    4. Nevermind

>>> """)
                if a == "1":
                    print('\x1b[1;37;40m' + "What are some of the commands or apps I can say?" + '\x1b[0m')
                    time.sleep(s)
                    print("""you can say things like:
                    map - gives a list of all your available locations
                    contacts - give a list of all your friends
                    call Uber - calls your Uber driver to pick you up
                    wallet - shows what's in your inventory
                    look around - gives a description of your current area
                    go to ___ - goes to a certain area in your present location to meet someone
                    hey ___ - talks to someone in your present location""")
                elif a == "2":
                    print('\x1b[1;37;40m' + "I just wanted to talk to you." + '\x1b[0m')
                    while True:
                        time.sleep(s)
                        r = input("""about what?
    1. What's the weather today?
    2. Why are we on this earth?
    3. Do you want to be friends, Simi?
    4. Nevermind

>>> """)
                        if r == "1":
                            print('\x1b[1;37;40m' + "What's the weather today?" + '\x1b[0m')
                            time.sleep(s)
                            print("the weather is nice.")
                            break
                        elif r == "2":
                            print('\x1b[1;37;40m' + "Why are we on this earth?" + '\x1b[0m')
                            time.sleep(s)
                            print("that's an answer you're going to have to find yourself.")
                            time.sleep(s)
                            print("I'm just a character in a dating simulator.")
                            break
                        elif r == "4":
                            print('\x1b[1;37;40m' + "Nevermind." + '\x1b[0m')
                            time.sleep(s)
                            print("yep, everything's okay.")
                            #leaves conversation
                            break
                        elif r == "3":
                            print('\x1b[1;37;40m' + "Do you want to be friends, Simi?" + '\x1b[0m')
                            time.sleep(s)
                            #will call a speech check if trying to be friends with simi
                            if simi not in friends:
                                while True:
                                    a = input("""really? do you mean it?
\x1b[1;33;40m1. Yes! Of course.\x1b[0m
2. No, I was just kidding!

    >>> """)
                                    if a == "1":
                                        print('\x1b[1;37;40m' + "Yes! Of course." + '\x1b[0m')
                                        time.sleep(s)
                                        k=random.randint(1,2)
                                        #if the player has talked to themselves positively, they can convince anyone with whatever they say
                                        if "self confidence" in inventory:
                                            k = 2
                                        if k == 1:
                                            print("hm, I don't believe you.")
                                            time.sleep(s)
                                            break
                                        else:
                                            print("wow, I've never made a friend before.")
                                            time.sleep(s)
                                            print("I can import my house number onto this phone then.")
                                            time.sleep(s)
                                            print("I'm so happy we can be friends.")
                                            time.sleep(1)
                                            print("I am now your friend!")
                                            friends.append(simi)
                                            break
                                    elif a == "2":
                                        print('\x1b[1;37;40m' + "No, I was just kidding!" + '\x1b[0m')
                                        time.sleep(s)
                                        print("okay...")
                                        break
                                break
                            else:
                                #is called if you're already friends with simi
                                print("don't be silly, we're already friends!")
                                break
                    break
                elif a == "3":
                    print('\x1b[1;37;40m' + "I need some help." + '\x1b[0m')
                    while True:
                        time.sleep(s)
                        r = input("""some things you can ask me:
    1. how many friends can i make?
    2. how many locations can i find?
    3. what are the chances of passing each speech check?
    4. how can i raise my charisma?
    5. how can i date one of the characters?
    6. that's all.

>>> """)
                        time.sleep(1)
                        if r == "1":
                            print("in this version of the game, you can make 7 friends in total.")
                        elif r == "2":
                            print("in this version of the game, there are 3 locations in total.")
                        elif r == "3":
                            print("green speech checks are 75%")
                            time.sleep(1)
                            print("yellow speech checks are 50%")
                            time.sleep(1)
                            print("red speech checks are 25%")
                        elif r == "4":
                            print("charisma isn't really a stat that you can level up,")
                            time.sleep(1)
                            print("but i hear those who are most confident love themselves first.")
                        elif r == "5":
                            print("sorry to disappoint, but this is actually a friendship simulator.")
                            time.sleep(1)
                            print("we're keeping this game e for everyone.")
                            time.sleep(1)
                            print("if you'd like to date, try to do so in real life.")
                        elif r == "6":
                            print("okay.")
                            break

                elif a == "4":
                    print('\x1b[1;37;40m' + "Nevermind." + '\x1b[0m')
                    time.sleep(s)
                    print("yep, everything's okay.")
                    break

                else:
                    print(f"hmm, i'm not finding anything for '{a}'.")
        elif character == abby:
            if abby in friends:
                print("\x1b[5;31;40mHi friend!\x1b[0m")
            elif abby in acquaintances:
                while True:
                    r = input("""\x1b[5;31;40mDid you get Paul's number for me?\x1b[0m
    1. Yeah I got the number right here.
    2. Not yet.
    3. Why do you want Paul's number so much?

>>> """)
                    if r == "1":
                        print('\x1b[1;37;40m' + "Yeah I got the number right here." + '\x1b[0m')
                        time.sleep(s)
                        if paul in friends:
                            print("\x1b[5;31;40mOh my god, thank you so much!\x1b[0m")
                            time.sleep(s)
                            print("\x1b[5;31;40mHere's my number.\x1b[0m")
                            time.sleep(s)
                            print("Abby is now your friend!")
                            friends.append(abby)
                            acquaintances.remove(abby)
                            break
                        else:
                            while True:
                                r = input("""You obviously don't have Paul's number. What do you say?
    1. Haha, just kidding!
    \x1b[1;31;40m2. His number is...(give a fake number)\x1b[0m

>>> """)
                                if r == "1":
                                    print('\x1b[1;37;40m' + "Haha, just kidding!" + '\x1b[0m')
                                    time.sleep(s)
                                    print("\x1b[5;31;40mThat's not a funny joke...\x1b[0m")
                                    break
                                elif r == "2":
                                    print("you think of a random phone number off the top of your head and tell her.")
                                    time.sleep(s)
                                    n=random.randint(100,999)
                                    m=random.randint(100,999)
                                    l=random.randint(1000,9999)
                                    print(f"\x1b[1;31;40m2. His number is ({n}) {m}-{l}.\x1b[0m")
                                    time.sleep(s)
                                    k=random.randint(1,4)
                                    if "self confidence" in inventory:
                                        k = 1
                                    if k == 1:
                                        print("\x1b[5;31;40mOh my god, thank you so much!\x1b[0m")
                                        time.sleep(s)
                                        print("\x1b[5;31;40mHere's my number.\x1b[0m")
                                        time.sleep(s)
                                        print("she actually believed you.")
                                        time.sleep(s)
                                        print("Abby is now your friend!")
                                        friends.append(abby)
                                        acquaintances.remove(abby)
                                        break
                                    else:
                                        print("\x1b[5;31;40mThat's definitely a fake number.\x1b[0m")
                                        time.sleep(s)
                                        print("\x1b[5;31;40mTalk to me when you have his actual number.\x1b[0m")
                                        break
                            break
                    elif r == "2":
                        print('\x1b[1;37;40m' + "Not yet." + '\x1b[0m')
                        time.sleep(s)
                        print("\x1b[5;31;40mCome back to me when you do.\x1b[0m")
                        break
                    elif r == "3":
                        print('\x1b[1;37;40m' + "Why do you want Paul's number so much?" + '\x1b[0m')
                        time.sleep(s)
                        print("\x1b[5;31;40mBecause he's so cool!\x1b[0m")
                        break
                    else:
                        print("\x1b[5;31;40mI don't get what you're saying.\x1b[0m")
            elif abby in enemies:
                while True:
                    r = input("""\x1b[5;31;40mWhat do you want, poser?\x1b[0m
    1. I wanna skate with you.
    2. I want to be your friend.
    3. Nothing.

>>> """)
                    if r == "1":
                        print('\x1b[1;37;40m' + "I wanna skate with you." + '\x1b[0m')
                        time.sleep(s)
                        print("\x1b[5;31;40mSorry, I don't skate with posers.\x1b[0m")
                        break
                    elif r == "2":
                        print('\x1b[1;37;40m' + "I want to be your friend." + '\x1b[0m')
                        time.sleep(s)
                        print("\x1b[5;31;40mHm, I'll consider it.\x1b[0m")
                        time.sleep(s)
                        print("\x1b[5;31;40mIf you can get me the boy's phone number over there, I'll give you mine.\x1b[0m")
                        time.sleep(s)
                        print("she points towards the \x1b[4;37;40mvolleyball net\x1b[0m, where a boy is practicing a jumping serve.")
                        enemies.remove(abby)
                        acquaintances.append(abby)
                        break
                    elif r == "3":
                        print('\x1b[1;37;40m' + "Nothing." + '\x1b[0m')
                        time.sleep(s)
                        print("\x1b[5;31;40mThen leave.\x1b[0m")
                        break
                    else:
                        print("\x1b[5;31;40mWhat are you saying? Just leave me alone.\x1b[0m")
                        break
            else:
                acquaintances.append(abby)
                while True:
                    r = input("""\x1b[5;31;40mHey, I'm kinda busy. What do you want?\x1b[0m
    1. Can I get your number?
    2. Oh I actually am really good at skating. I could help you out!
    3. Oh, nothing.

>>> """)
                    if r == "1":
                        print('\x1b[1;37;40m' + "Can I get your number?" + '\x1b[0m')
                        time.sleep(s)
                        print("\x1b[5;31;40mYeah sure, here you go.\x1b[0m")
                        time.sleep(s)
                        print("Abby is now your friend!")
                        friends.append(abby)
                        acquaintances.remove(abby)
                        break
                    elif r == "2":
                        print('\x1b[1;37;40m' + "Oh I actually am really good at skating. I could help you out!" + '\x1b[0m')
                        time.sleep(s)
                        print("\x1b[5;31;40mReally? That'd be great. Can you tell me what I'm doing wrong?\x1b[0m")
                        while True:
                            time.sleep(s)
                            r = input("""You realize you actually don't know how to skate. What do you do?
    1. Have you tried jumping higher?
    2. You need to 'shuv' your board faster.
    3. You're 'popping' too softly.
    \x1b[1;31;40m4. It's better if I just show you.\x1b[0m

>>> """)
                            if r == "1":
                                print('\x1b[1;37;40m' + "Have you tried jumping higher?" + '\x1b[0m')
                                time.sleep(s)
                                print("\x1b[5;31;40mSeriously? Just cuz I'm jumping higher doesn't mean my technique is clean.\x1b[0m")
                                time.sleep(s)
                                print("well that could have gone better...")
                                enemies.append(abby)
                                acquaintances.remove(abby)
                                break
                            elif r == "2":
                                print('\x1b[1;37;40m' + "You need to 'shuv' your board faster." + '\x1b[0m')
                                time.sleep(s)
                                print("\x1b[5;31;40mI'm obviously trying to ollie, not pop-shuv it.\x1b[0m")
                                time.sleep(s)
                                print("well that could have gone better...")
                                enemies.append(abby)
                                acquaintances.remove(abby)
                                break
                            elif r == "3":
                                print('\x1b[1;37;40m' + "You're 'popping' too softly." + '\x1b[0m')
                                time.sleep(s)
                                print('\x1b[1;37;40m' + "Do it harder for more height." + '\x1b[0m')
                                time.sleep(s)
                                print("\x1b[5;31;40mWow! That really works. Thanks!\x1b[0m")
                                time.sleep(s)
                                print("\x1b[5;31;40mHere, just in case I need more skate help, let's exchange numbers!\x1b[0m")
                                time.sleep(s)
                                print("Abby is now your friend!")
                                friends.append(abby)
                                acquaintances.remove(abby)
                                break
                            elif r == "4":
                                print('\x1b[1;37;40m' + "It's better if I just show you." + '\x1b[0m')
                                time.sleep(s)
                                print('\x1b[1;37;40m' + "Let me have your skateboard for a sec." + '\x1b[0m')
                                time.sleep(s)
                                k=random.randint(1,4)
                                print("you get on her skateboard and attempt to ollie for the very first time in your life...")
                                if "self confidence" in inventory:
                                    k = 1
                                if k == 1:
                                    print("and you succeed!")
                                    time.sleep(s)
                                    print("you put what you learned from playing 'tony hawk pro skater' to good use and land with steez.")
                                    time.sleep(s)
                                    print("\x1b[5;31;40mAmazing! That was the sickest ollie I've ever seen!\x1b[0m")
                                    time.sleep(s)
                                    print("\x1b[5;31;40mI didn't really learn anything, but here's my number!\x1b[0m")
                                    time.sleep(s)
                                    print("\x1b[5;31;40mCall me up if you ever wanna schedule a skate sesh.\x1b[0m")
                                    time.sleep(s)
                                    print("Abby is now your friend!")
                                    friends.append(abby)
                                    acquaintances.remove(abby)
                                    break
                                else:
                                    print("and you fail...")
                                    time.sleep(s)
                                    print("i guess riding your cousin's pennyboard up & down the block 4 years ago wasn't enough.")
                                    time.sleep(s)
                                    print("\x1b[5;31;40mThat was hella sketchy. I don't think you actually know how to skate.\x1b[0m")
                                    enemies.append(abby)
                                    acquaintances.remove(abby)
                                    break
                            else:
                                print('\x1b[5;31;40m' + "What did you say?" + '\x1b[0m')
                        break
                    elif r =="3":
                        print('\x1b[1;37;40m' + "Oh, nothing." + '\x1b[0m')
                        time.sleep(s)
                        print("\x1b[5;31;40mAlright.\x1b[0m")
                        acquaintances.remove(abby)
                        break

                    else:
                        print("\x1b[5;31;40mWhat? Sorry, I can't understand you.\x1b[0m")
        elif character == paul:
            if paul in friends:
                print('\x1b[5;32;40m' + f"What's up, {myself.name}?" + '\x1b[0m')
            elif paul in acquaintances:
                while True:
                    r = input("""\x1b[5;32;40mWhere's my 5 buck lunch?\x1b[0m
    1. Right here.
    2. Sorry, I don't have it yet.
    3. Why do you like Dairy Queen so much?

>>> """)
                    if r == "1":
                        print('\x1b[1;37;40m' + "Right here." + '\x1b[0m')
                        time.sleep(s)
                        if "5 buck lunch" in inventory:
                            print("you give Paul the 5 buck lunch.")
                            inventory["5 buck lunch"] = 0
                            time.sleep(s)
                            print("\x1b[5;32;40mThanks!\x1b[0m")
                            time.sleep(s)
                            print("\x1b[5;32;40mHave my number. Let's go to Dairy Queen together sometime.\x1b[0m")
                            time.sleep(s)
                            print("Paul is now your friend!")
                            acquaintances.remove(paul)
                            friends.append(paul)
                            break
                        else:
                            print("\x1b[5;32;40mNo you don't; stop playing.\x1b[0m")
                            break
                    elif r == "2":
                        print('\x1b[1;37;40m' + "Sorry, I don't have it yet." + '\x1b[0m')
                        time.sleep(s)
                        print("\x1b[5;32;40mBetter actually buy it, don't waste my money.\x1b[0m")
                        break
                    elif r == "3":
                        print('\x1b[1;37;40m' + "Why do you like Dairy Queen so much?" + '\x1b[0m')
                        time.sleep(s)
                        print("\x1b[5;32;40mBecause it tastes so good.\x1b[0m")
                        break
                    else:
                        print("\x1b[5;32;40mWatchu say?\x1b[0m")
            else:
                while True:
                    r = input("""\x1b[5;32;40mWhat do you need?\x1b[0m
    1. Can we be friends?
    2. Nice serves.
    3. Nevermind.

>>> """)
                    if r == "1":
                        acquaintances.append(paul)
                        print('\x1b[1;37;40m' + "Can we be friends?" + '\x1b[0m')
                        time.sleep(s)
                        print("\x1b[5;32;40mSure! Only if you buy me 5 buck lunch at Dairy Queen though.\x1b[0m")
                        time.sleep(s)
                        map["dairyqueen"] = "Dairy Queen"
                        print("Dairy Queen has been added to your map!")
                        time.sleep(s)
                        print("\x1b[5;32;40mHere's some money to buy it.\x1b[0m")
                        time.sleep(s)
                        inventory['dollars'] += 5
                        print("$5 have been added to you wallet!")
                        time.sleep(s)
                        print("say \x1b[3;37;40mwallet\x1b[0m to see what's in your inventory.")
                        break
                    elif r == "2":
                        print('\x1b[1;37;40m' + "Nice serves." + '\x1b[0m')
                        time.sleep(s)
                        print("\x1b[5;32;40mThanks.\x1b[0m")
                        break
                    elif r == "3":
                        print('\x1b[1;37;40m' + "Nevermind." + '\x1b[0m')
                        time.sleep(s)
                        print("Paul goes back to practicing his serves.")
                        break
                    else:
                        print("\x1b[5;32;40mWatchu say?\x1b[0m")
    else:
        print("that person isn't here.")

while True:
    #s is the variable in most time.sleep() instances, whichever number the player chooses will set the game text speed
    s = input("""\x1b[1;37;40mAt what speed would you like the text to show?\x1b[0m
    1. Normal
    2. Fast
    3. Super Fast (developer speed)
    \x1b[1;37;40m(type in the number)\x1b[0m
>>> """)
    if s == "1":
        s = 2
        break
    elif s == "2":
        s = 1
        break
    elif s == "3":
        s = 0
        break
    else:
        print("invalid response")
        time.sleep(1)
print('\x1b[5;35;40m' + "Hi! Welcome to the dating simulator!" + '\x1b[0m')
#the purple italized text is set for Colette's dialogue; right now this is an automatic encounter to get the player introduced to someone
time.sleep(s)
#makes sure the text doesn't pop in all at once, giving the player a chance to read everything
print('\x1b[5;35;40m' + "Well, it's more like a friendship simulator because you won't really be dating much." + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + "But there'll be a lot of people for you to meet and befriend!" + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + "I'm the tutorial lady, and I'll be teaching you the basics of making friends!" + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + "Now, can you tell me your name?" + '\x1b[0m')
time.sleep(s)
myself.name = input("\n>>> ")
#the player can choose their name
time.sleep(1)
while True:
    ny = input(f"""\x1b[5;35;40mIs {myself.name} really your name?\x1b[0m
    1. Yes
    2. No

>>> """)
    if ny == "1":
        print("Yes.")
        time.sleep(s)
        break
    elif ny == "2":
        print("No.")
        time.sleep(s)
        print('\x1b[5;35;40m' + "It isn't? I must've heard you wrong. What's your name, again?" + '\x1b[0m')
        time.sleep(s)
        myself.name = input(">>> ")
        time.sleep(1)
        ny = input(f"""\x1b[5;35;40m{myself.name} is your name, right?\x1b[0m
    1. Yes
    2. No

>>> """)
        if ny == "1":
            print("Yes.")
            time.sleep(s)
            break
        elif ny == "2":
            print("No.")
            time.sleep(s)
            print('\x1b[5;35;40m' + f"This is too much. I think I'll just call you {myself.name}." + '\x1b[0m')
            time.sleep(s)
            break
        #this feature is just for humor
        elif ny !="1":
            print('\x1b[5;35;40m' + "Excuse me? Sorry, I don't quite get what you mean" + '\x1b[0m')
            time.sleep(1)
    elif ny !="1":
        print('\x1b[5;35;40m' + "Excuse me? Sorry, I don't quite get what you mean" + '\x1b[0m')
        time.sleep(1)
#the loop allows for the player to make sure they get the name they want (at least with a single try)
print('\x1b[5;35;40m' + f"Hi, {myself.name}! Nice to meet you!" + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + f"Now, normally people won't approach and talk to you like I just did." + '\x1b[0m')
time.sleep(s)
print("\x1b[5;35;40mI'll stand in the \x1b[0m" + "\x1b[4;35;40mcorner\x1b[0m" + "\x1b[5;35;40m of the room.\x1b[0m")
time.sleep(s)
print('\x1b[5;35;40m' + f"Here, pretend like I didn't already say hi. How would you initiate a conversation?" + '\x1b[0m')
time.sleep(1)
print("\x1b[1;37;40mwhen talking to someone for the first time, you need to approach & introduce yourself.\x1b[0m")
time.sleep(1)
print("\x1b[1;37;40msay \x1b[0m\x1b[3;37;40mgo to corner\x1b[0m\x1b[1;37;40m to walk up to the girl in the corner.\x1b[0m")
time.sleep(1)
while True:
    a = input(">>> ").lower()
    if a == "go to corner":
        approach("corner")
        break
time.sleep(s)
print("\x1b[1;37;40many word that is underlined is a location you can approach.\x1b[0m")
time.sleep(1)
print("\x1b[1;37;40mif you want to learn more about your surroundings or get a refresher on what can be found there, say \x1b[0m\x1b[3;37;40mlook around\x1b[0m\x1b[1;37;40m.\x1b[0m")
time.sleep(2)
while True:
    a = input(">>> ").lower()
    if a == "look around":
        observe()
        break
print("\x1b[1;37;40mnow that you know her name, you can greet her and begin a conversation.\x1b[0m")
time.sleep(1)
print("\x1b[1;37;40msay \x1b[0m\x1b[3;37;40mhey Colette\x1b[0m\x1b[1;37;40m to greet Colette.\x1b[0m")
time.sleep(1)
print("\x1b[1;37;40m(other greetings besides \x1b[0m\x1b[3;37;40mhey\x1b[0m\x1b[1;37;40m might work. feel free to try some others.)\x1b[0m")
#a system message to be more direct
time.sleep(1)
while True:
    a=input(">>> ").lower()
    for x in greetings:
        if a == f"{x} colette":
            talkto(colette)
    if colette not in acquaintances:
        break
if colette in enemies:
    time.sleep(s)
    print("\x1b[1;37;40myou look on the floor and see that Colette dropped something on her way out.\x1b[0m")
    time.sleep(s)
    print("It's a cellphone!")
    time.sleep(s)
    print("\x1b[1;37;40myou turn it on, realizing it has no password.\x1b[0m")
    time.sleep(s)
    print("I might as well keep this to help me get out of here.")
    time.sleep(s)
    print("I should call an Uber to pick me up.")
    time.sleep(s)
    map["joecollinspark"] = "Joe Collins Park"
    print("\x1b[1;37;40msay \x1b[0m\x1b[3;37;40mcall Uber\x1b[0m\x1b[1;37;40m.\x1b[0m")
    while True:
        a = input(">>> ").lower()
        if a == "call uber" or a == "call uber driver":
            call_uber()
            break
        else:
            print("I need to call an Uber to get out of here.")
            time.sleep(1)
#the most important loop, this is what will prompt the player for what command to input
while True:
    time.sleep(s)
    #checks to see if you acquired all 7 friends in the game
    if len(friends) == 7:
        win()
    #checks to see if you insulted yourself, if you do, stops options from coming up
    elif "major depression" in heart:
        print("\x1b[1;37;40mwell, you didn't kill yourself,\x1b[0m")
        time.sleep(s)
        print("\x1b[1;37;40mbut now you're too sad & insecure to talk to anyone.\x1b[0m")
        time.sleep(s)
        print("\x1b[1;37;40mgame over?\x1b[0m")
        time.sleep(s)
        dead()
    else:
        options()