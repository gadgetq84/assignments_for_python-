num1 = int(input("введите первое число списка: "))
step = int(input("введите шаг прогрессии: "))
count = int(input("введите кол-во элементов в списке: "))
mylist = list()
mylist = [num1+i*step for i in range(1,count)]
print("Список элементов арифметической прогрессии: ")
print(mylist)