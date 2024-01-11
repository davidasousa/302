import random

matches = 0
iterations = 10000

for jdx in range(iterations):
    date_count = {day:0 for day in range(1,366)} # Defining A Count Dictionary For Each Date
    for idx in range(0,50):
        date_count[random.randint(1,365)] += 1 # Now The Counts Are Filled Out
    for count in date_count.values():
        if count >= 2:
            matches += 1
            break

print("The Odds That In A Group Of Fifty People Two Have The Same Birthday Is: ", matches / iterations)
