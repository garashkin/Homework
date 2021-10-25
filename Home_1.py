# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_itn = 35
my_float = 20.21
my_str = 'Hello, world'
my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}
my_bool = True
my_list = [2, 1]

list = [my_itn, my_float, my_str, my_dict, my_bool, my_list]

for i in list:

    print(f'{i} is {type(i)}')
