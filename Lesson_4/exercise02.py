"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""

result = []
list = [int(i) for i in input("Введите любые числа разделенные пробелом: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i - 1]:
        (result.append(list[i]))

print("элементы исходного списка, "
      "значения которых больше предыдущего элемента: ", result)