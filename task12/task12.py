from datetime import datetime
s = int(input("введите число S сумма чисел "))
p = int(input("введите число P произведение чисел "))
start_time = datetime.now()
for i in range(s):
    for j in range(p):
        if s == i+j and p == i*j:
            print(f"{s}={i+j} {p}={i*j}")
            print(f"Возможно это числа {i}, {j}")
print(datetime.now() - start_time)