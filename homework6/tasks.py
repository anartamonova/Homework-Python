# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
# a_1 = int(input("a1=  "))
# d= int(input("d=  "))
# count= int(input("count=  "))


# def progress (a_1, d, count):
#     res = []
#     for i in range(count):
#         res.append(a_1+i*d)
#     print(res)
        
# progress (a_1, d, count)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_list = int(input("min = "))
max_list = int(input("max = "))
new_list = []
for i in range(len(list)):
    if list[i] < min_list or list[i] > max_list :
        new_list.append(i)
print(new_list)