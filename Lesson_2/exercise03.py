# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_in_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_in_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input("Введите месяц в виде целого числа от 1 до 12: "))

if 1 <= month <= 2 or month == 12:
    print("через lis>> ", seasons_in_list[0])
    print("через dict>> ", seasons_in_dict.get(1))
elif 3 <= month <= 5:
    print("через lis>> ", seasons_in_list[1])
    print("через dict>> ", seasons_in_dict.get(2))
elif 6 <= month <= 8:
    print("через lis>> ", seasons_in_list[2])
    print("через dict>> ", seasons_in_dict.get(3))

elif 9 <= month <= 11:
    print("через lis>> ", seasons_in_list[3])
    print("через dict>> ", seasons_in_dict.get(4))

else:
    print("Введите число Только от 1 до 12")
