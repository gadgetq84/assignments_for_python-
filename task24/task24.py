import random;
list1 = []

ml1 = int(input("введите колличество кустов в грядке: "))
# функция для заполнения списка 
def GenNewList(count,mylist):
    for i in range(count):
        mylist.append(random.randint(1,50))
GenNewList(ml1,list1)

count = 0
max_count=0
print(f"Исходный список {list1}")
for i in range(len(list1)):
    count = list1[i-2]+list1[i-1]+list1[i]
    if max_count<count:
        max_count = count
    
    print (f"Урожай с каждого прохода {list1[i-2]}+{list1[i-1]}+{list1[i]} ={count}")

print (f"Максимальное кол-во урожая с куста и двух соседних {max_count}")