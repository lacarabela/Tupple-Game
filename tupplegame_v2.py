#three dice rolled
#any number of players
#two dice match are locked, three match no score
#can reroll others as often as player likes
#Other Rules:
#   Score displayed between rounds
#   play to 50
#   AI player will reroll 3s and lower and will try to catch up in score if behind
#   Game high score displayed at end and start of each game

import random

def die_roll():
    return random.randint(1,6)

def player_choice():
    d1 = die_roll()
    d2 = die_roll()
    d3 = die_roll()
    if d1 == d2 and d2 == d3:
        print("You have terrible luck and have an opening Tupple for zero points")
        return 0
    while True:
        choice = input("You Rolled a "+str(d1)+","+str(d2)+", and "+str(d3)+"\nWould you like to (T)apout or (R)eroll")
        if choice == "T":
            return d1+d2+d3
        elif choice == "R":
            if d1 == d2:
                d3 = die_roll()
                print("Your Dice are"+str(d1)+","+str(d2)+", and "+str(d3))
                if d1 == d2 and d2 == d3:
                    print("You got a Tupple, lose all points")
                    return 0
            elif d1 == d3:
                d2 = die_roll()
                print("Your Dice are"+str(d1)+","+str(d2)+", and "+str(d3))
                if d1 == d2 and d2 == d3:
                    print("You got a Tupple, lose all points")
                    return 0
            elif d2 == d3:
                d1 = die_roll()
                print("Your Dice are"+str(d1)+","+str(d2)+", and "+str(d3))
                if d1 == d2 and d2 == d3:
                    print("You got a Tupple, lose all points")
                    return 0
            else:
                reroll = input ("Which index values would you like to reroll: (1,2,3) ?")
                if '1' in reroll:
                    d1 = die_roll()
                if '2' in reroll:
                    d2 = die_roll()
                if '3' in reroll:
                    d3 = die_roll()
                print("You Rolled a "+str(d1)+","+str(d2)+", and "+str(d3)+"")
                if d1 == d2 and d2 == d3:
                    print("You got a Tupple, lose all points")
                    return 0
def ai_choice(scoretobeat):
    d1 = die_roll()
    d2 = die_roll()
    d3 = die_roll()
    if d1 == d2 and d2 == d3:
        print("Computer has terrible luck and opened with a Tupple for zero points")
        return 0
    while True:
        print("Computer Rolled a "+str(d1)+","+str(d2)+", and "+str(d3)+".\n")
        if d1+d2+d3 > scoretobeat:
            print("Computer has taken the "+str(d1+d2+d3)+" points!")
            return d1+d2+d3
        if d1 == d2:
            d3 = die_roll()
            print("Computer Dice are"+str(d1)+","+str(d2)+", and "+str(d3))
            if d1 == d2 and d2 == d3:
                print("Computer got a Tupple, lose all points")
                return 0
        elif d1 == d3:
            d2 = die_roll()
            print("Computer Dice are"+str(d1)+","+str(d2)+", and "+str(d3))
            if d1 == d2 and d2 == d3:
                print("Computer got a Tupple, lose all points")
                return 0
        elif d2 == d3:
            d1 = die_roll()
            print("Computer Dice are"+str(d1)+","+str(d2)+", and "+str(d3))
            if d1 == d2 and d2 == d3:
                print("Computer got a Tupple, lose all points")
                return 0
        else:
            if d1<4:
                d1 = die_roll()
            if d2<4:
                d2 = die_roll()
            if d3<4:
                d3 = die_roll()
            print("Computer Rolled a "+str(d1)+","+str(d2)+", and "+str(d3)+"")
            if d1+d2+d3>12:
                return d1+d2+d3
            if d1 == d2 and d2 == d3:
                print("You got a Tupple, lose all points")
                return 0
        
choice = input("How many players would you like to play(enter a number), \nor would you like to play against the (C)omputer")
if choice == "C":
    print("Picked C")
    winner = False
    playerscores = [0,0]
    while winner == False:
        print(playerscores)
        playerscores[0] += player_choice()
        if playerscores[0] >= 50:
            print("Player wins this round!")
            winner = True
        playerscores[1] += ai_choice(playerscores[0])
        if playerscores[1] >= 50:
            print("Computer wins this round!")
            winner = True

else:
    playerscores = [0 for i in range(int(choice))]
    print(playerscores)
    winner = False
    while winner == False:
        player = 0
        while player < int(choice):
            print(player)
            playerscores[player] += player_choice()
            if playerscores[player] >= 50:
                print("Player "+str(player)+" wins this round!")
                winner = True
            print (playerscores)
            player += 1
