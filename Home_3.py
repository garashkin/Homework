# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_list = ['Зима', 'Весна', 'Лето', 'Осень']
month_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month_number = int(input('Введите номер месяца: '))
if month_number == 1 or month_number == 2 or month_number == 12:
    print(month_dict.get(1))
    print(month_list[0])
elif month_number == 3 or month_number == 4 or month_number == 5:
    print(month_dict.get(2))
    print(month_list[1])
elif month_number == 6 or month_number == 7 or month_number == 8:
    print(month_dict.get(3))
    print(month_list[2])
elif month_number == 9 or month_number == 10 or month_number == 11:
    print(month_dict.get(4))
    print(month_list[3])
else:
    print('Нет такого месяца')