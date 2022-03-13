'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

with open('test_2.txt', 'r') as my_file:
    content = my_file.read()
    print(f'Содержимое файла: \n {content} ____________')


with open('test_2.txt', 'r') as my_file:
    content = my_file.readlines()
    print(f'Количество строк в файле - {len(content)}')
    for i in range(len(content)):
        print(f'Окличество символов в {i + 1}-ой строке {len(content[i])}')

with open('test_2.txt', 'r') as my_file:
    content = my_file.read()
    content = content.split()
    print(f'Общее количество слов - {len(content)}')

