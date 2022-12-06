# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.
#     *Пример:* 
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     - k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
#*Доп задание: значения коэффициентов от -100 до 100

from random import randint
k = int(input('Введите степень k = '))
lst = []
for i in range(k + 1):
    lst.append(randint(0, 101)) 

str='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(lst) if j][::-1])

str=str.replace('x^1+', 'x+')
str=str.replace('x^0', '')
str=(str + '=0')
with open('Task4.txt', 'w') as data:
         data.write(str)