# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число N = "))
a = num
lst = []
n = 2
while num > 1:
    if num % n == 0:
        lst.append(n)
        num = num/n
    else:
        n += 1
print(f'Список простых множителей числа {a}: {lst}')