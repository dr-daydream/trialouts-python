#           pseudo random

import random

x = random.randint(1,9)
y = random.random()

choices = ["rock", "paper", "scissors"]
z = random.choice(choices)

cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(cards)

print(cards)