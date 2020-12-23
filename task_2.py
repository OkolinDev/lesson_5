# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

f_obj = open('test_task2.txt', 'r', encoding="utf-8")
content = len(f_obj.readlines())
print(f'Колличество строк в файле: {content}')
f_obj.close()
f_obj = open('test_task2.txt', 'r', encoding="utf-8")
rez = f_obj.readlines()
for letter in rez:
    letters = letter.split()

    print(f'Колличество слов в строке: {len(letters)}')
f_obj.close()


