def schitalka(rhyme):
    rhymelist = rhyme.lower().split()
    def f(x): return sum(1 for i in x if i in 'аеёиоуыэюя')
    tmp = f(rhymelist[0])
    if all([f(i) == tmp for i in rhymelist]):
        return 'Парам пам-пам'
    else:
        return 'Пам парам'


print(schitalka("пара-ра-рам рам-пам-папам\
 па-ра-па-да"))
