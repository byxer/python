# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*
# *Доп задание: для разного размера уравнения

from random import randint
k = int(input('Введите степень k = '))

lst = []
for i in range(k + 1):
    lst.append(randint(0, 101)) 
str='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(lst) if j][::-1])
str=str.replace('x^1+', 'x+')
str=str.replace('x^0', '')
str=(str + '=0')
with open('Task5_1.txt', 'w') as data:
         data.write(str)

lst2 = []
for i in range(k + 1):
    lst2.append(randint(0, 101)) 
str2='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(lst2) if j][::-1])
str2=str2.replace('x^1+', 'x+')
str2=str2.replace('x^0', '')
str2=(str2 + '=0')
with open('Task5_2.txt', 'w') as data:
         data.write(str2)

with open('Task5_1.txt', 'r') as data:
    st1 = data.readlines()
with open('Task5_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Многочлен №1 {st1}")
print(f"Многочлен №2 {st2}")

l = len(lst)
if len(lst) > len(lst2):
    l = len(lst2)
lst3 = [lst[i] + lst2[i] for i in range(l)]
if len(lst) > len(lst2):
    mm = len(lst)
    for i in range(l,mm):
        lst3.append(lst[i])
else:
    mm = len(lst2)
    for i in range(l,mm):
        lst3.append(lst2[i])
str3='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(lst3) if j][::-1])
str3=str3.replace('x^1+', 'x+')
str3=str3.replace('x^0', '')
str3=(str3 + '=0')
with open('Task5_3.txt', 'w') as data:
         data.write(str3)

with open('Task5_3.txt', 'r') as data:
    st3 = data.readlines()
print(f"Сумма многочленов = {st3}, записана в файле: Task5_3.txt")