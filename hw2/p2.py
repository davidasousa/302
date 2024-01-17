import numpy as np
import random
import matplotlib.pyplot as plt

charlieData = np.zeros(6)
davidData = np.zeros(6)

for i in range(0,10000):
    r = random.randint(0,599)

    if r < 60:
        charlieData[0] += 1
    elif r < 180:
        charlieData[1] += 1
    elif r < 360:
        charlieData[2] += 1
    elif r < 480:
        charlieData[3] += 1
    elif r < 540:
        charlieData[4] += 1
    elif r < 600:
        charlieData[5] += 1

    if r < 180:
        davidData[0] += 1
    elif r < 240:
        davidData[1] += 1
    elif r < 300:
        davidData[2] += 1
    elif r < 360:
        davidData[3] += 1
    elif r < 480:
        davidData[4] += 1
    elif r < 600:
        davidData[5] += 1

plt.bar(range(1, len(charlieData) + 1), charlieData, edgecolor='black')
plt.title("Charlie's Dice")
plt.show()
plt.savefig("Charlie.png")
plt.clf

plt.bar(range(1, len(davidData) + 1), davidData, edgecolor='black')
plt.title("David's Dice")
plt.show()
plt.savefig("David.png")
plt.clf
