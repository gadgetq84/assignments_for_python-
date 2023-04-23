num1 = int(input("введите первое число: "))
num2 = int(input("введите второе число: "))


def mysums(numb1, numb2) -> int:
    if numb2 == 0:
        return numb1
    else:
        return mysums(numb1+1, numb2-1)

print(f"{num1} + {num2} = {mysums(num1, num2)}")
