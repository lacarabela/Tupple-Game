#three dice rolled
#any number of players
#two dice match are locked, three match no score
#can reroll others as often as player likes
#Other Rules:
#   Score displayed between rounds
#   play to 50
#   AI player will reroll 3s and lower and will try to catch up in score if behind
#   Game high score displayed at end and start of each game

import random #imported so random numbers can be generated

def die_roll():
    return random.randint(1,6)#random die roll 1-6

def display_dice(d1, d2, d3): # This is repeated a few times, so I made a function for it
    print(f"Dice: {d1}, {d2}, {d3}")

def handle_tupple(player_num, current_score): # This is repeated a few times, so I made a function for it
    print(f"Player {player_num}, you rolled a tupple and score zero points!")
    return 0

def player_choice(player_num, score):#gets player Number and that players current score from the main implementation
    d1 = die_roll()
    d2 = die_roll()
    d3 = die_roll()
    if d1 == d2 and d2 == d3:
        return handle_tupple(player_num, score)
    while True:
        choice = input("Player: "+player_num+", (your current score is "+score+") you Rolled a "+str(d1)+","+str(d2)+", and "+str(d3)+"\nWould you like to (T)apout or (R)eroll")
        if choice == "T" or choice == "t":
            return d1 + d2 + d3
        elif choice == "R" or choice =="r":
            if d1 == d2:#if matching pair won't give the option of dice to roll
                d3 = die_roll()
                display_dice(d1, d2, d3)
                if d1 == d2 and d2 == d3:
                    return handle_tupple(player_num, score)
            elif d1 == d3:#if matching pair won't give the option of dice to roll
                d2 = die_roll()
                display_dice(d1, d2, d3)
                if d1 == d2 and d2 == d3:
                    return handle_tupple(player_num, score)
            elif d2 == d3:#if matching pair won't give the option of dice to roll
                d1 = die_roll()
                display_dice(d1, d2, d3)
                if d1 == d2 and d2 == d3:
                    return handle_tupple(player_num, score)
            else:
                reroll = input ("Which index values would you like to reroll: (1,2,3) ?")#done this way so it can take almost any version of user input for choices, 123, 1,2,3, 1 2 3, etc.
                if '1' in reroll:
                    d1 = die_roll()
                if '2' in reroll:
                    d2 = die_roll()
                if '3' in reroll:
                    d3 = die_roll()
                display_dice(d1, d2, d3)
                if d1 == d2 and d2 == d3:
                    return handle_tupple(player_num, score)

def ai_choice(score_to_beat):#Ai choice reuses the rule logic and will only try to catch up to the player, gets the players score as a benchmark the computer will use to make its choices, will only reroll
    d1 = die_roll()
    d2 = die_roll()
    d3 = die_roll()
    if d1 == d2 and d2 == d3:
        print("Computer has terrible luck and opened with a Tupple for zero points")
        return 0
    while True:
        display_dice(d1, d2, d3)
        if d1+d2+d3 > score_to_beat:
            print("Computer has taken the "+str(d1+d2+d3)+" points!")
            return d1+d2+d3
        if d1 == d2:
            print("Computer Dice are "+str(d1)+","+str(d2)+", and "+str(d3)+", the computer doesn't like risks and takes the points!")
            return d1+d2+d3
        elif d1 == d3:
            print("Computer Dice are "+str(d1)+","+str(d2)+", and "+str(d3)+", the computer doesn't like risks and takes the points!")
            return d1+d2+d3
        elif d2 == d3:
            print("Computer Dice are "+str(d1)+","+str(d2)+", and "+str(d3)+", the computer doesn't like risks and takes the points!")
            return d1+d2+d3
        else:
            if d1<4:
                d1 = die_roll()
            if d2<4:
                d2 = die_roll()
            if d3<4:
                d3 = die_roll()
            if d1+d2+d3>12:
                print("Computer Rolled is happy with "+str(d1)+","+str(d2)+", and "+str(d3)+" for "+str(d1+d2+d3)+" points!")
                return d1+d2+d3
            if d1 == d2 and d2 == d3:
                print("Computer got a Tupple, and lost all points")
                return 0
        
choice = input("How many players would you like to play(enter a number), \nor would you like to play against the (C)omputer")
if choice == "C" or choice == "c":
    print("Picked C")
    winner = False
    player_scores = [0,0]
    while winner == False:
        print("Human Score: "+str(player_scores[0])+" Computer Score: "+str(player_scores[1]))
        player_scores[0] += player_choice("Human", str(player_scores[0]))
        if player_scores[0] >= 50:#check if winner, condition is 50 points or more
            print("Player wins this round!")
            winner = True
            break
        player_scores[1] += ai_choice(player_scores[0])
        if player_scores[1] >= 50:#check if winner, condition is 50 points or more
            print("Computer wins this round!")
            winner = True
            break

else:
    playerscores = [0 for i in range(int(choice))]#enumerate any number of players, even very large amounts, which are not recommended
    print(playerscores)
    winner = False
    while winner == False:#keep playing until there is a winner
        player = 0
        while player < int(choice):
            print(player)
            playerscores[player] += player_choice(str(player),str(playerscores[player]))
            if playerscores[player] >= 50:#check if winner, condition is 50 points or more
                print("Player "+str(player)+" wins this round!")
                winner = True
                break
            print (playerscores)
            player += 1
