# список римских чисел
numbers = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


# ф-я конвертирующая арабское число в римское
def convert_to_roman(num):
    roman_number = ''

    while num > 0:
        for arab, rom in numbers:
            while num >= arab:
                roman_number += rom
                num -= arab

    return roman_number


# ф-я для конвертации чисел больше 4000
def convert_to_roman_over_4000(num):
    thousands, divider = divmod(num, 1000)
    return "({}){}".format(convert_to_roman(thousands), convert_to_roman(divider))


# ф-я для проверки числа и выбора ф-ии конвертации
def to_roman(num):
    if num >= 4000:
        return convert_to_roman_over_4000(num)
    else:
        return convert_to_roman(num)


# ф-я запуска
def action_to_roman(word):
    while word != "0":
        print(to_roman(int(word)))
        word = input("Чтобы продолжить просто введите новое число или нажмите 0 , чтобы сменить действие: ")
