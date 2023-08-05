import os
from functions import notebook
import text
from consolemenu import myconsolemenu

Currentdir = os.getcwd()
noteb = notebook("notes.csv", Currentdir)
myaddressbook = noteb.read_file()
mygeneralmenu = myconsolemenu(text.menu_options)

def show_generalmenu():
    mygeneralmenu.print_menu()
    myselections = mygeneralmenu.enter_your_choice()
    return myselections

# обработчик событий выбора пунктов меню
def action_selected(number):
    if number == 1:
        os.system('cls')
        noteb.print_data()
    elif number == 2:
        os.system('cls')
        noteb.add_entry()
        os.system('cls')
        noteb.print_data()
    elif number == 3:
        os.system('cls')
        noteb.print_data()
        noteb.delete_entry()
    elif number == 4:
        os.system('cls')
        noteb.print_data()
        noteb.change_entry()
        os.system('cls')
        noteb.print_data()
    elif number == 5:
        os.system('cls')
        noteb.find_records()
    elif number == 6:
        os.system('cls')
        noteb.write_file()
    elif number == 7:
        os.system('cls')
        noteb.save_changes_check()
        exit()
    else:
        os.system('cls')
        noteb.show_message(text.error_menumsg, 'error')
