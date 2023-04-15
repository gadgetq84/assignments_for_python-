my_word = input("введите слово: ").upper()

enru_dict= dict()
#  создаем компактный словарь где в качастве ключей будем использовать картежи
enru_dict = {("A", "E", "I", "O", "U", "L", "N", "S", "T", "R" , "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"):1,
           ("D", "G", "Д", "К", "Л", "М", "П", "У"):2,
           ( "B", "C", "M", "P","Б", "Г", "Ё", "Ь", "Я"):3,
           ("F", "H", "V", "W", "Y", "Й", "Ы" ):4,
           ("K", "Ж", "З", "Х", "Ц", "Ч"):5,
           ("J", "X","Ш", "Э", "Ю"):8,
           ("Q", "Z","Ф", "Щ", "Ъ"):10
           }
# Переделываем наш словарь в нормальный вид key:value
temp_dict = {key:value for keys, value in enru_dict.items() for key in keys}
cost=0
for i in range(len(my_word)):
    if temp_dict.get(my_word[i]):
        cost +=temp_dict[my_word[i]]

print(f"стоимость введенного cлова {cost}")
