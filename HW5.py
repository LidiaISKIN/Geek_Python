"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""

# my_f = open('filo.txt', 'w')
# line = input('Введите текст \n')
# while line:
#     my_f.writelines(line)
#     line = input('Введите текст \n')
#     if not line:
#         break
#
# my_f.close()
# my_f = open('filo.txt', 'r')
# content = my_f.readlines()
# print(content)
# my_f.close()

"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке."""

# my_file = open('file_2_1.txt', 'r')
# content = my_file.read()
# print(f'Содержимое файла: \n {content}')
# my_file = open('file_2_1.txt', 'r')
# content = my_file.readlines()
# print(f'Количество строк в файле - {len(content)}')
# my_file = open('file_2_1.txt', 'r')
# content = my_file.readlines()
# for i in range(len(content)):
#     print(f'Koличество символов {i + 1} - ой строки {len(content[i])}')
# my_file = open('file_2_1.txt', 'r')
# content = my_file.read()
# content = content.split()
# print(f'Общее количество слов - {len(content)}')
# my_file.close()

"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников."""

# with open('sal.txt', 'r') as my_file:
#     sal = []
#     poor = []
#     my_list = my_file.read().split('\n')
#     for i in my_list:
#         i = i.split()
#         if int(i[1]) < 20000:
#            poor.append(i[0])
#         sal.append(i[1])
# print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')

"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл."""
# - * - coding: utf - 8 -*-
# rus = {'One' : '1_r', 'Two' : '2_r', 'Three' : '3_r', 'Four' : '4_r'}
# new_file = []
# with open('input.txt', 'r') as file_obj:
#     # русский не поддерживается в ОС ноута
#     for i in file_obj:
#         i = i.split(' ', 1)
#         new_file.append(rus[i[0]] + '  ' + i[1])
#     print(new_file)
#
# with open('output.txt', 'w') as file_obj_2:
#     file_obj_2.writelines(new_file)

"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

# def summary():
#     try:
#         with open('task_5.txt', 'w+') as file_obj:
#             line = input('Введите цифры через пробел \n')
#             file_obj.writelines(line)
#             my_numb = line.split()
#
#             print(sum(map(int, my_numb)))
#     except IOError:
#         print('Ошибка в файле')
#     except ValueError:
#         print('Неправильно набран номер. Ошибка ввода-вывода')
# summary()

"""6. Необходимо создать (не программно) текстовый файл, 
где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран."""

# subj = {}
# with open('raspisanie.txt', 'r') as init_file:
#     for line in init_file:
#         subject, lecture, practice, lab = line.split()
#         subj[subject] = int(lecture) + int(practice) + int(lab)
#     print(f'Общее количество часов по предмету - \n {subj}')

"""пример файла
inf 100 50 2
inf9 100 50 2
inf8 100 50 2 
"""

"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, 
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('task_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('task_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')