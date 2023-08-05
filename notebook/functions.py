import datetime
from color import style
import text
import csv


class notebook:
    def __init__(self, filename: str, current_dir: str) -> None:
        self.__filename = filename
        self.__current_dir = current_dir
        self.__notebook = list()

    def show_message(self, string: str, type: str, border=1):
        mycolor = style.YELLOW
        if "error" in type:
            mycolor = style.RED
        elif "info" in type:
            mycolor = style.YELLOW
        elif "ok" in type:
            mycolor = style.GREEN
        else:
            mycolor = style.WHITE

        if border == 1:
            print('\n' + mycolor + '*'*len(string))

        print(mycolor + string + style.WHITE)

        if border == 1:
            print(mycolor + '*'*len(string)+'\n' + style.WHITE)

    def input_message(self, string: str, color=style.YELLOW):
        return input(color + string + style.WHITE)

    def input_note(self):
        result = []
        result.append(self.input_message(text.text_add_title, style.YELLOW))
        result.append(self.input_message(
            text.text_add_description, style.YELLOW))
        result.append(f"{datetime.datetime.now():%d-%m-%Y/%H:%M}")
        return result
    

# Читаем файл и загоняем контент в лист
    def read_file(self):
        try:
            with open(self.__current_dir+"\\"+self.__filename, "r", encoding='utf-8') as self.file_read:
                reader = csv.reader(
                    self.file_read, delimiter=';', skipinitialspace=True)
                self.__notebook = list(reader)
                # сортировка листа по полю даты 
                self.__notebook.sort(key=lambda element: int(datetime.datetime.strptime(element[2], "%d-%m-%Y/%H:%M").timestamp()))
            return self.__notebook
        except FileNotFoundError:
            self.show_message(text.text_file_notexist, 'error', 1)
            self.write_file()
            return self.__notebook


# конвертируем лист в нормальный формат для записи в файл а-ля csv

    def write_file(self):
        with open(self.__current_dir+"\\"+self.__filename, "w", newline='', encoding='utf-8') as self.__file_write:
            writer = csv.writer(self.__file_write,
                                delimiter=';', skipinitialspace=True)
            # self.__sep = "::"
            # for item in self.__addressbook:
            #     self.__file_write.write("%s\n" % self.__sep.join(item))
            writer.writerows(self.__notebook)
        self.show_message(text.text_ready, 'ok', 1)


# простая смпатяшная печаталка на экран листов ... старался не использовать сторонние модули

    def print_data(self, printlist=''):

        printlist = printlist if len(printlist) > 0 else self.__notebook

        print(style.YELLOW+"{:<5} {:<20} {:<40} {:<15}".format(
            'id', 'Заголовок события', 'Описание', 'дату/время создания'))
        for index, item in enumerate(printlist):
            print(style.WHITE+"{:<5} {:<20} {:<40} {:<15}".format(
                index, item[0], item[1], item[2]))

# функция удаления записи в листе
    def delete_entry(self):
        self.__delitem = ''
        try:
            self.__delitem = int(
                self.input_message(text.text_delete_rec, style.YELLOW))
            self.show_message(str(self.__delitem)+" " +
                              text.text_ready_delete, 'ok', 1)
            if 0 <= self.__delitem <= len(self.__notebook):

                ret_val = self.__notebook.pop(self.__delitem)

                self.show_message(" ".join(ret_val)+" " +
                                  text.text_ready_delete, 'ok', 1)

        except:
            self.show_message(text.text_add_error2, 'error', 1)


# функция добавление новой записи


    def add_entry(self):
        self.__additem = []
        try:
            self.__additem = self.input_note()
            # self.__additem = list(map(str, self.input_message(
            #     text.text_add_entry, style.YELLOW).split(" ", 4)))
            if len(self.__additem) == 3:
                self.__notebook.append(self.__additem)
                self.show_message(text.text_add_succsess, 'ok', 1)
                # print(text.text_add_succsess)
            else:
                self.show_message(text.text_add_error, 'error', 1)
                # print(text.text_add_error)
        except:
            self.show_message(text.text_add_error2, 'error', 1)
            # print(text.text_add_error2)

# функция изменения  записи
    def change_entry(self):
        self.__iditem = int
        self.__changeitem = ''
        try:
            self.__iditem = int(
                self.input_message(text.text_change_entry, style.YELLOW))

            if 0 <= self.__iditem <= len(self.__notebook):
                self_oldrecords = self.__notebook[self.__iditem]
                self.show_message(text.text_change_entry3 +
                                  " ".join(self_oldrecords), 'info', 1)
                # self.__notebook[self.__iditem] = list(
                #     map(str, self.input_message(text.text_change_entry2, style.WHITE).split(" ", 4)))
                self.__notebook[self.__iditem] = self.input_note()

        except:
            self.show_message(text.text_change_error, 'error', 1)
            # print(text.text_change_error)
            input(text.text_change_error2)

# функция поиска записи
    def find_records(self):
        self.__searchitem = str
        self.__ressearch = list()
        self.__searchitem = self.input_message(
            text.text_find_rec, style.YELLOW)
        if self.__searchitem:
            # for item in self.__addressbook:
            self.__ressearch = list(
                filter(lambda x: self.__searchitem in " ".join(x), self.__notebook))
            if len(self.__ressearch) > 0:
                self.print_data(self.__ressearch)
            else:
                self.show_message(text.text_find_error, 'error', 1)
                # print(text.text_find_error)


# функция спрашивает выгрузить все в файл или нет

    def save_changes_check(self):
        self.__choice = str(
            self.input_message(text.text_save_changes, style.YELLOW))
        if 'да' in self.__choice or not self.__choice:
            self.write_file()
            self.show_message(text.text_save_succsess, 'ok', 1)
            # print(style.GREEN+text.text_save_succsess)
        else:
            self.show_message(text.text_save_error, 'error', 1)
            # print(style.RED+text.text_save_error)
