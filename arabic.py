# список римских чисел
numbers = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
           (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, 'I')]


# ф-я которая конвертирует римское число в арабское
def number_to_arabic(word):
    index = 0
    roman_int = 0
    for integer, romanNumeral in numbers:
        while word[index: index + len(romanNumeral)] == romanNumeral:
            roman_int += integer
            index += len(romanNumeral)
    return roman_int


# запуск конвертации
def action_to_arabic(word):
    while word != '0':
        print(number_to_arabic(word.upper()))
        word = input("Чтобы продолжить просто введите новое число или нажмите 0 , чтобы сменить действие: ")
