import os
from functions import phonebook
import text
from consolemenu import myconsolemenu

Currentdir = os.getcwd()
addressbook = phonebook("book.txt", Currentdir)
myaddressbook = addressbook.read_file()
mygeneralmenu = myconsolemenu(text.menu_options)

def show_generalmenu():
    mygeneralmenu.print_menu()
    myselections = mygeneralmenu.enter_your_choice()
    return myselections

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
        os.system('cls')
        addressbook.show_message(text.error_menumsg, 'error')
