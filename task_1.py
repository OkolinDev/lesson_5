
# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


f_obj = open('task_1test.txt', 'w', encoding='utf-8')

while True:
    user_input = input('Введите данные:\n')

    f_obj.write(f'{user_input}\n')
    if user_input == '':
        break

f_obj.close()

