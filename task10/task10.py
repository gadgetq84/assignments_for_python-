import random;
coins = []
def GenNewArray(count,myarray):
    for i in range(count):
        coins.append(random.randint(0,1))
#заполнили список случайно .. 0 решкой а 1  гербом
GenNewArray(16,coins)
print(*coins)
print(coins.count(0) if coins.count(0) < coins.count(1) else coins.count(1))