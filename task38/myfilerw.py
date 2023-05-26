from color import style

# родился такой класс но не нравится что в нем присутствуют элементы меню ... надо вынести часть кода в класс consolemenu


class filerw:
    def __init__(self, filename: str, current_dir: str) -> None:
        self.__filename = filename
        self.__current_dir = current_dir
        self.__addressbook = list()

# Читаем файл и загоняем контент в лист
    def read_file(self):
        with open(self.__current_dir+"\\"+self.__filename, "r", encoding='utf-8') as self.file_read:
            self.__addressbook = list(
                map(lambda x: list(x.split("::")), self.file_read.read().splitlines()))
        return self.__addressbook

# конвертируем лист в нормальный формат для записи в файл а-ля csv
    def write_file(self):
        with open(self.__current_dir+"\\"+self.__filename, "w", encoding='utf-8') as self.__file_write:
            self.__sep = "::"
            for item in self.__addressbook:
                self.__file_write.write("%s\n" % self.__sep.join(item))
        print('Готово')

# простая смпатяшная печаталка на экран листов ... старался не использовать сторонние модули
    def print_data(self, printlist=''):

        printlist = printlist if len(printlist) > 0 else self.__addressbook

        print(style.YELLOW+"{:<5} {:<15} {:<10} {:<15} {:<15} {:<15}".format(
            'id', 'Фамилия', 'Имя', 'Отчество', 'Телефон', 'Комментарий'))
        for index, item in enumerate(printlist):
            print(style.WHITE+"{:<5} {:<15} {:<10} {:<15} {:<15} {:<15}".format(
                index, item[0], item[1], item[2], item[3], item[4]))

# функция удаления записи в листе
    def delete_entry(self):
        self.__delitem = ''
        try:
            self.__delitem = int(
                input(style.YELLOW+'Введите ID записи которую нужно удалить:'+style.WHITE))
            if 0 <= self.__delitem <= len(self.__addressbook):
                ret_val = self.__addressbook.pop(self.__delitem)
                print(*ret_val, "Удалена")
        except:
            print('Что-то не то. Выберите корректный ID ...')

# функция добавление новой записи
    def add_entry(self):
        self.__additem = []
        try:
            self.__additem = list(map(str, input(
                style.YELLOW+"Введите через пробел Фамалию,Имя,Отчество,номер телефона,комментарий: "+style.WHITE).split(" ", 4)))
            if len(self.__additem) == 5:
                self.__addressbook.append(self.__additem)
                print("Запись добавлена!!!")
            else:
                print("Запись не добавлена!!! Не хватает чего то!!!")
        except:
            print('Что то не то. Выберите корректный ID ...')

# функция изменения  записи
    def change_entry(self):
        self.__iditem = int
        self.__changeitem = ''
        try:
            self.__iditem = int(
                input(style.YELLOW+'Введите ID записи которую нужно изменить:'+style.WHITE))

            if 0 <= self.__iditem <= len(self.__addressbook):
                self_oldrecords = self.__addressbook[self.__iditem]

                print(style.RED+"Редактируем: "+" ".join(self_oldrecords))

                self.__addressbook[self.__iditem] = list(map(str, input(
                    style.YELLOW+"Введите через пробел новые данные: "+style.WHITE).split(" ", 4)))

        except:
            print('Что-то не то. Выберите корректный ID ...')
            input("Нажми Enter для продолжения")

# функция поиска записи
    def find_records(self):
        self.__searchitem = str
        self.__ressearch = list()
        self.__searchitem = input(
            style.YELLOW+'Введите строку для поиска:'+style.WHITE)
        if self.__searchitem:
            # for item in self.__addressbook:
            self.__ressearch = list(
                filter(lambda x: self.__searchitem in " ".join(x), self.__addressbook))
            if len(self.__ressearch) > 0:
                self.print_data(self.__ressearch)
            else:
                print("Сорян( Ничего не найдено!!!")


# функция спрашивает выгрузить все в файл или нет
    def save_changes_check(self):
        self.__choice = str(
            input(style.YELLOW+"Хотите сохранить изменения в файл (default:да) (да/нет)?:") or 'да')
        if 'да' in self.__choice:
            self.write_file()
            print(style.GREEN+"пи-па-по-пу Изменения сохранены")
        else:
            print(style.RED+"Изменения не сохранены")
