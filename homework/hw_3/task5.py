# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:

#     - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

num = int(input('Введите чило = '))

def fib (n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

def rev_fib(n):
    return (-1) ** (n + 1) * fib(n)

lst = []
for i in range(num + 1):
    lst.append(rev_fib(i))
lst.reverse()
lst.pop(-1)
for i in range(num + 1):
    lst.append(fib(i))
print(lst)