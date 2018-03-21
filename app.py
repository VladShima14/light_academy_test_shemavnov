import roman
import arabic

print("Добро пожаловать в конвертирующее приложение ")
print("Нажмите 1 , если вам нужно римское число сконвертировать в арабское")
print("Нажмите 2 , если вам нужно арабское число сконвертировать в римское")
print("Чтобы закончить работу приложения , напишите exit")
app_action = input("Ваш выбор: ")


# ф-я активации приложения
def convert_app(act):
    while act != 'exit':
        if act == '1':
            app_word = input("Введите римское число: ")
            arabic.action_to_arabic(app_word.upper())
        elif act == '2':
            app_word = input("Введите арабское число: ")
            roman.action_to_roman(app_word)
        else:
            act = input("Вы ошиблись , повторите попытку")

        act = input("Ваш выбор: ")


convert_app(app_action)
