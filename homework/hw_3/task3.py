# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример:
#     - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(len(lst)):
    lst[i] -= int(lst[i])
print(round(max(lst) - min(lst), 2))