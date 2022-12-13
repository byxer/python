# Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# #Старое решение
# num = int(input('Введите число = '))
# f = 1
# for i in range(num):
#     i = i + 1
#     f = i * f
#     print(f, end=" ,")

#Новое решение
from math import factorial
num = int(input('Введите число = '))
f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
lst = list( f(i) for i in range(1, num +1))
print(lst)