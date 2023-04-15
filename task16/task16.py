n = int(input("введите колличество элементов в списке: "))
my_list = []
# функция для заполнения списка 
def GenNewList(count,mylist):
    for i in range(count):
        mylist.append(i+1)
# заполнили список значениями
GenNewList(n,my_list)

print(*my_list)
x = int(input("введите число X для поиска: "))
# вывели результат
print(f"{my_list.count(x)} раз встречается")