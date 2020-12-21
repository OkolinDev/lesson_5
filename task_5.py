# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def summa():
    try:
        with open('task5.txt', 'w+', encoding='UTF-8') as f_obj:
            line = input('Вводите цифры через пробел \n')
            f_obj.writelines(line)
            number = line.split()
            print(sum(map(float, number)))

    except IOError:
        print('Ошибка в файле: не существует, диск переполнен.')

    except ValueError:
        print('Недопустимые данные.')


summa()
