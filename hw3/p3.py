import random

categories = [[] for i in range(5)]

categories[0] = [70, 80, 90, 100] # HW
categories[1] = [50, 60, 70, 80, 90, 100] # Oh My Question
categories[2] = [60, 70, 80] # Midterm 1
categories[3] = [40, 50, 60] # Midterm 2
categories[4] = [30, 40, 50, 60] # Final

counts = [0] * 8

for i in range(100000):
    finalscore = -1
    category = random.randint(1,100)

    if category <= 10:
        finalscore = categories[0][random.randint(0,3)]
    elif category <= 30:
        finalscore = categories[1][random.randint(0,4)]
    elif category <= 50:
        finalscore = categories[2][random.randint(0,2)]
    elif category <= 70:
        finalscore = categories[3][random.randint(0,2)]
    else:
        finalscore = categories[4][random.randint(0,3)]

    counts[(finalscore // 10) - 3] += 1

print("Percent Chance Of Getting A 30 On A Category Is", (counts[0] / 100000))
print("Percent Chance Of Getting A 40 On A Category Is", (counts[1] / 100000))
print("Percent Chance Of Getting A 50 On A Category Is", (counts[2] / 100000))
print("Percent Chance Of Getting A 60 On A Category Is", (counts[3] / 100000))
print("Percent Chance Of Getting A 70 On A Category Is", (counts[4] / 100000))
print("Percent Chance Of Getting A 80 On A Category Is", (counts[5] / 100000))
print("Percent Chance Of Getting A 90 On A Category Is", (counts[6] / 100000))
print("Percent Chance Of Getting A 100 On A Category Is", (counts[7] / 100000))

avgScore = ((30 * counts[0]) / 100000 + (40 * counts[1]) / 100000 + (50 * counts[2]) / 100000 + (60 * counts[3]) / 100000 + (70 * counts[4]) / 100000 + (80 * counts[5]) / 100000 + (90 * counts[6]) / 100000 + (100 * counts[7]) / 100000)

print(avgScore)
