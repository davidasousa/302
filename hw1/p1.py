import random

count = 0
iterations = 100000

for idx in range(0,iterations):
    i = random.randint(1,26)
    j = random.randint(1,26)

    while j == i:
        j = random.randint(1,26)

    if i >= 6 and j < 6:
        count += 1
    if j >= 6 and i < 6:
        count += 1

print("The Probability Of A Random Consonant And Vowel Consecutivly Or Vice Versa Is ", count / iterations)
