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
    return random.randint(1,6)#random die roll 1-6

def player_choice(playernum, score):
    d1 = die_roll()
    d2 = die_roll()
    d3 = die_roll()
    if d1 == d2 and d2 == d3:
        print("Player Number "+playernum+", you have terrible luck and have an opening Tupple for zero points!")#in case a player opens with a tupple
        return 0
    while True:
        choice = input("Player Number "+playernum+", (your current score is"+score+") you Rolled a "+str(d1)+","+str(d2)+", and "+str(d3)+"\nWould you like to (T)apout or (R)eroll")
        if choice == "T":
            return d1+d2+d3
        elif choice == "R":
            if d1 == d2:#if matching pair won't give the option of dice to roll
                d3 = die_roll()
                print("Your Dice are"+str(d1)+","+str(d2)+", and "+str(d3))
                if d1 == d2 and d2 == d3:
                    print("You got a Tupple, lose all points")
                    return 0
            elif d1 == d3:#if matching pair won't give the option of dice to roll
                d2 = die_roll()
                print("Your Dice are"+str(d1)+","+str(d2)+", and "+str(d3))
                if d1 == d2 and d2 == d3:
                    print("You got a Tupple, lose all points")
                    return 0
            elif d2 == d3:#if matching pair won't give the option of dice to roll
                d1 = die_roll()
                print("Your Dice are"+str(d1)+","+str(d2)+", and "+str(d3))
                if d1 == d2 and d2 == d3:
                    print("You got a Tupple, lose all points")#rolling into a tupple
                    return 0
            else:
                reroll = input ("Which index values would you like to reroll: (1,2,3) ?")#done this way so it can take almost any version of user input for choices, 123, 1,2,3, 1 2 3, etc.
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
def ai_choice(scoretobeat):#Ai choice reuses the rule logic and will only try to catch up to the player
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
        playerscores[0] += player_choice(str(0), str(playerscores[0]))
        if playerscores[0] >= 50:
            print("Player wins this round!")
            winner = True
            break
        playerscores[1] += ai_choice(playerscores[0])
        if playerscores[1] >= 50:
            print("Computer wins this round!")
            winner = True
            break

else:
    playerscores = [0 for i in range(int(choice))]#enumerate any number of players, even very large amounts, which are not recommended
    print(playerscores)
    winner = False
    while winner == False:
        player = 0
        while player < int(choice):
            print(player)
            playerscores[player] += player_choice(str(player),str(playerscores[player]))
            if playerscores[player] >= 50:
                print("Player "+str(player)+" wins this round!")
                winner = True
                break
            print (playerscores)
            player += 1
