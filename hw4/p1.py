import random
# Generate Random Number With random.randint(a,b) - a and b both inclusive

class part:
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.failed = False

pcParts = [ part("CPU", 364.00), part("MotherBoard", 231.58),
            part("Ram", 114.99), part("Cooler", 99.99),
            part("SSD", 99.99), part("PSU", 99.99) ]

avgCosts = 0

for idx in range(100000):
    repairCosts = 0
    for years in range(5):
        for partIdx in range(6):
            if pcParts[partIdx].failed == True: # Parts Only Break Once
                continue

            if random.randint(1,10) == 1:
                pcParts[partIdx].failed = True
                repairCosts += pcParts[partIdx].price

    # Resetting The Failed Value For A New Test
    for part in pcParts:
        part.failed = False

    avgCosts += repairCosts

print("The total repair costs after 5 years would be ", avgCosts / 100000)




