# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
# def expon (x,y):
#     if y == 0:
#         return 1
#     elif x == 0:
#         return 0
#     return x * expon(x,y-1)

# a = int(input("a= "))
# b = int(input("b= "))

# print(expon(a,b))

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def sum (x,y):
    if x==0:
        return y
    return sum(x-1,y+1)

a = int(input("a= "))
b = int(input("b= "))

print(sum(a,b))