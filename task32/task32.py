import random
min = int(input("введите минимум: "))
max = int(input("введите максимум: "))

# функция для заполнения списка 
def GenNewList(count,mylist):
    for i in range(count):
        mylist.append(random.randint(-10,10))
mylist = []
GenNewList(20,mylist)
print(f"Исходный лист {mylist}")
count=0
reslist  = [i for i in range(len(mylist)) if min<= mylist[i] <=max]
print(f"Индексы элементов принадлежащих заданному диапазону:  {reslist}")