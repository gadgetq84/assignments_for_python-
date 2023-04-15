n = int(input("введите колличество элементов в списке: "))
my_list = []
# функция для заполнения списка 
def GenNewList(count,mylist):
    for i in range(count):
        mylist.append(i+1)
GenNewList(n,my_list)
print(*my_list)
x = int(input("введите число X для поиска: "))
# вывели результат
# Вишенка на тортике min(my_list,key=lambda i:abs(i-x)) где lambda i:abs(i-x) Лямбда-функция
print(f"Самый близкий по величине элемент к заданному числу {x} это {min(my_list,key=lambda i:abs(i-x))}")