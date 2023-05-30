import os
from color import style
import text

class myconsolemenu:
    def __init__(self, menu_list=[]) -> None:
        self.__menulist = menu_list
        self.__menulen = len(menu_list)

    def print_menu(self):
        print(style.YELLOW+text.menu_header1)
        for i, value in enumerate(self.__menulist, start=1):
            print(style.RED+f"{i}."+style.GREEN+f" {value}")

    def enter_your_choice(self):
        self.__option = ''
        
        try:
            self.__option = int(input(style.YELLOW+text.menu_selected_descr+style.WHITE))
            if 1 <= self.__option <= self.__menulen:
                return self.__option

        except:
            print(text.error_menumsg2)
            return -1
