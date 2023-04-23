num = int(input("введите число: "))
deg = int(input("введите степень: "))


def exponent(numb, degr) -> int:
    """Возвращает число numb в степени degr
    Args:
        numb (int): Число
        degr (int): Степень

    Returns:
        int: возвращает numb в степени degr
    """
    if degr == 0:
        return 1
    if degr == 1:
        return numb
    else:
        return numb * exponent(numb, degr-1)

print(f"{num} в степени {deg} = {exponent(num, deg)}")
