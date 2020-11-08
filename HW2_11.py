"""1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

my_list = [1, 'cte', 'b', 4, 5, 'p', [2, 3, 4], (4, 5), {4, 6, 7}]
i = 0
for elem in my_list:
    i = type(elem)
    print(i)

"""2. Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input()."""

count_el = int(input('введите количество элементов в списке'))
my_list = []
i = 0
elem = 0
while i < count_el:
    my_list.append(input('Введите следующее значение списка'))
    i += 1
for elem in range(int(len(my_list)//2)):
        my_list[elem], my_list[elem+1] = my_list [elem+1], my_list[elem]
        elem += 2
print(my_list)

"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict."""
#
seasons_list = ('winter',
                'spring',
                'summer',
                'fall')
seasons_dict = {'winter': (12,1,2),
                'spring': (3,4,5),
                'summer': (6,7,8),
                'fall':(9,10,11),
                }
seasons_dict_2 = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'fall',
    10: 'fall',
    11: 'fall'
}
user_month_num = int(input("enter num for month"))

season_idx = user_month_num // 3 % 4

for key, value in seasons_dict.items():
    if user_month_num in value:
        print(key)
        break
print(season_idx)
print (seasons_list[season_idx])

"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
Если в слово длинное, выводить только первые 10 букв в слове."""

string = input("Enter a phrase")
word = []
num = 1
for elem in range(string.count(' ') + 1):
    word = string.split()
    if len(str(word)) <= 10:
        print (f"{num} {word [elem]}")
        num += 1
    else:
        print(f"{num} {word [elem] [0:10]}")
        num +=1

string = input("Enter a phrase")

for elem, word in enumerate(string.split(' ')):
    print (f"{elem}:{word[:10]}")

"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""

my_list = [7,5,3,3,2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число из списка или (13 - выход)"))
while digit !=13:
        for i in range(len(my_list)):
            if my_list[i] == digit:
                my_list.insert(0, digit)
                break
            elif my_list[0] < digit:
                my_list.insert(0, digit)
            elif my_list[-1] > digit:
                my_list.append(digit)
            elif my_list[i] > digit and my_list[i + 1] < digit:
                my_list.insert(i + 1, digit)
        print(f"текущий список - {my_list}")
        digit = int(input("Введите число"))
##тут точно что-то не так, могу посмотреть чужие решения, но дождусь разбора задачи

"""6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами 
(характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. 
Реализовать словарь, в котором каждый ключ — характеристика товара, 
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}"""

product_tamplate = {
    'title':("product name", str),
    'cost':("cost of product", str),
    'count':("count of product", str),
    'unit':("units", str),
}

next_enter = True

auto_inc = 1
product_list = []

while next_enter:
    product ={}
    for key, value in product_tamplate.items():
        while True:
            user_value = input(f'{value[0]}\n')
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f'{e}\n Не верное значение данных')
                continue
            product[key] =user_value
            break
    product_list.append((auto_inc, product))
    auto_inc +=1

    while True:
        next_add = input("Добавить еще продукт? да/нет\n")
        if next_add.lower() in ('да', 'нет'):
            next_enter = next_add.lower() == 'да'
            break
        else:
            print ('неверный ввод, повторите')

print (f"{product_list}")

product_analytics ={}

for key in product_tamplate:
    result = []
    for itm in product_list:
        result.append(itm[1][key])
    product_analytics[key] = result

print (product_analytics)