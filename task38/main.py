import os
from consolemenu import myconsolemenu
from myfilerw import filerw

menu_options = [
    'Отобразить телефонный справочник', # открыть справочник
    'Добавить запись', # добавить запись в лист
    'Удалить запись', # удалить запись в листе
    'Редактировать запись', # редактировать запись 
    'Поиск в телефонном справочнике', # поиск в листе
    'Сохранить',  # Сохранить в файл
    'Exit', # предложить сохраниться перед выходом
]

os.system('cls')
Currentdir = os.getcwd()
mygeneralmenu = myconsolemenu(menu_options)

addressbook = filerw("book.txt", Currentdir)
myaddressbook = addressbook.read_file()

# обработчик событий выбора пунктов меню
def action_selected(number):
        if number == 1:
            os.system('cls')
            addressbook.print_data()        
        elif number == 2:
            os.system('cls')
            addressbook.add_entry()
            os.system('cls')
            addressbook.print_data()
        elif number == 3:
            os.system('cls')
            addressbook.print_data()
            addressbook.delete_entry()
        elif number == 4:
            os.system('cls')
            addressbook.print_data()
            addressbook.change_entry()
            os.system('cls')
            addressbook.print_data()
        elif number == 5:
            os.system('cls')
            addressbook.find_records()
        elif number == 6:
            os.system('cls')
            addressbook.write_file()
        elif number == 7:
            os.system('cls')
            addressbook.save_changes_check()
            exit()
        else:
            print('Нет такого пункта меню!!!')


while (True):
    mygeneralmenu.print_menu()
    myselections = mygeneralmenu.enter_your_choice()
    action_selected(myselections)
