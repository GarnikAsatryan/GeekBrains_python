'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''


with open('test_5.txt', 'w+') as my_file:
    line = input('Введите цифры через пробел \n')
    my_file.writelines(line)
    my_numb = line.split()
    print(my_numb)

    print(sum(map(int, my_numb)))
