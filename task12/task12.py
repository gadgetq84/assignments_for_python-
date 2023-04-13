x = int(input("введите число X "))
y = int(input("введите число Y "))

for i in range(x):
    for j in range(y):
        if x == i+j and y == i*j:
            print(f"{x}={i+j} {y}={i*j}")
            print(f"Возможно это числа {i}, {j}")
