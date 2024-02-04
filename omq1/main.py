import random

cards = [
        "Ace","Ace","Ace","Ace",
        2,2,2,2,
        3,3,3,3,
        4,4,4,4,
        5,5,5,
        6,6,6,6,
        7,7,7,
        8,8,8,8,
        9,
        10,10,10,10,
        "Jack","Jack","Jack","Jack",
        "Queen","Queen","Queen","Queen",
        "King","King","King"]

val = 14
friendVal = 19
DealerVal = 16

# Part 1:
win = 0
exp_itr = 1000000

for i in range(exp_itr):
    card = cards[random.randint(0,len(cards) - 1)]
    if card == 7 or card == 6:
        win += 1

print("Chance Of Winning In The First Part Is:", win/exp_itr);

# Part 2
draw = 0

for i in range(exp_itr):
    card = cards[random.randint(0,len(cards) - 1)]
    if card == 5:
        draw += 1

print("Chance Of Tying Your Friend In The Second Part Is:", draw/exp_itr);





