"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""

my_f = open('filo.txt', 'w')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('filo.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()

"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке."""

my_file = open('file_2_1.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('file_2_1.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('file_2_1.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Koличество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('file_2_1.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников."""

with open('sal.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')

"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл."""
# - * - coding: utf - 8 -*-
rus = {'One' : '1_r', 'Two' : '2_r', 'Three' : '3_r', 'Four' : '4_r'}
new_file = []
with open('input.txt', 'r') as file_obj:
    # русский не поддерживается в ОС ноута
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('output.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)