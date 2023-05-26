import os
from color import style

class myconsolemenu:
    def __init__(self, menu_list=[]) -> None:
        self.__menulist = menu_list
        self.__menulen = len(menu_list)

    def print_menu(self):
        print(style.YELLOW+f"Меню телефонного справочника")
        for i, value in enumerate(self.__menulist, start=1):
            print(style.RED+f"{i}."+style.GREEN+f" {value}")

    def enter_your_choice(self):
        self.__option = ''
        
        try:
            self.__option = int(input(style.YELLOW+'Выберите номер пункта меню: '+style.WHITE))
            if 1 <= self.__option <= self.__menulen:
                return self.__option

        except:
            print('Что то не то. Выберите номер из меню ...')
            return -1
