# Tupple Dice README
## How to Run the Tupple Game:
Run the following command in terminal: 
```
python tupplegame_4.py
```
## Rules of the Game:
1. **Player Selection:**
    - You can play against any number of players. Enter a real number greater than 1 when prompted.
    - Alternatively, you can play a single-player game against a simple computer opponent by selecting "C".
2. **Starting the Game:**
    - Once the game starts, three dice will be rolled for each player.
    - The objective is to score as many points as possible each round to reach a total score of 50.
3. **Scoring Points:**
    - Points are scored based on the face value of all dice.
    - A round ends when the player either chooses to score their dice or if they roll three of a kind (resulting in zero points for that round).
4. **Rolling Dice:**
    - If you choose to reroll, paired dice will be locked in and cannot be rerolled.
    - You can only reroll the non-matching die.
    - If none of the dice match, you can select which dice to reroll by entering their indices (labeled 1, 2, and 3).
## Game Flow
- Each player takes turns rolling three dice.
- Players can choose to keep their current roll or reroll some of the dice to improve their score.
- If three of a kind are rolled, the player scores zero points for that round.
- The game continues until a player reaches a total score of 50 points.