# Урок 2. Циклы (for, while)
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0


n = int(input('Введите количество монет: '))
heads_count = 0
tails_count = 0

#c использованием рандомной подстановки чисел
from random import randint
coins_list = [randint(0, 1) for i in range(n) ] 
print(coins_list)
for q in range(n):
    if coins_list[q]==0 :
        tails_count += 1
    else:
        heads_count += 1

# ввод с клавиатуры
# for i in range(n):
#     coin = int(input('Введите 0, если монетка упала ребром, 1 - если гербом: '))
#     if coin==0 :
#         tails_count += 1
#     else:
#         heads_count += 1

# print(heads_count, tails_count)
if heads_count==n or tails_count==n:
    print(f'Все монеты лежат одинаковой стороной')
elif heads_count == tails_count:
    print(f'Количество монеток ребром и гербом одинаково')
elif tails_count > heads_count:
    print(f'Переверните {heads_count} монетки/монеток, которые лежат гербом')
else:
    print(f'Переверните {tails_count} монетки/монеток, которые лежат решкой')





# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

s = int(input('S---> '))
p = int(input('P---> '))
x = int()
y = int()
for x in range(s):
    for y in range(p):
        if x+y==s and x*y==p :
            print(f'x= {x}, y= {y} ')
           
            
           


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите число N: "))
i = 0
while i < n:
    if 2 ** i < n:
        print(2**i)
    i+=1
    
