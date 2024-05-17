#Jenny Zhong 

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random
import numpy as np

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

#loop

if p1 == p2:
    print("It's a tie!")
elif p1 == 'rock' and p2 == 'scissors': 
    print("Player 1 wins!")
elif p1 == 'paper' and p2 == 'scissors':
    print("Player 2 wins!")
elif p1 == 'scissors' and p2 == 'rock':
    print("Player 1 wins!")
elif p1 == 'paper' and p2 == 'rock': 
    print("Player 1 wins!")
elif p1 == 'scissors' and p2 == 'paper': 
    print("Player 1 wins!")
elif p1 == 'rock' and p2 == 'paper': 
    print("Player 2 wins!")

play_again = input("Play again? (y/n)")
if play_again == "y": 
    pass 
else: 
    print("End game")

#In class answer 
beats = {'rock':'scissors', 'paper': 'rock', 'scissors': 'paper'}
p1 = random.choices(choices)
P2 = random.choices(choices)
print(f'Player 1: {p1}\nPlayer 2: {p2}')

if beats[p1] == p2: 
    print('Player 1 wins!')
elif beats[p2] == p1: 
    print('Player 2 wins!')
else: 
    print('Tie')
    
#functions 

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

def find_winner(p1, p2): 
    if beats[p1] == p2:
        return 'Player 1 wins!'
    elif beats[p2] == p1:
        return 'Player 2 wins!'
    else: 
        return 'Tie'

def readysetgo():
    return random.choice(choices)

def play_once():
    p1 = readysetgo()
    p2 = readysetgo()
    print(f'Player 1: {p1}\nPlayer 2: {p2}')

    winner = find_winner(p1, p2)
    print(f'The winner is: {winner}')   

#classes   

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors:')
p2 = random.choice(choices)
 

class Player(): 
    def __init__(self, name, strategy='random'):
        self.name = name
        self.wins = 0
        self.choices = ['rock', 'paper', 'scissors']
        self.strategy = strategy
        
    def readysetgo(self): 
        if self.strategy == 'random': 
            return random.choice(self.choices)
        elif self.strategy == 'always_rock': 
            return 'rock'

class Game(): 
    def __init__(self, num_players=2): 
        self.beats = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
        self.num_players = num_players
        self.players = [Player(str(n+1)) for n in range(num_players)]
    
    def find_wniner(self, p1, p2): 
        if self.beats[p1] == p2: 
            return 'Player 1'
        elif self.beats[p2] == p1:
            return 'Player 2'
        else: 
            return 'Tie'













    