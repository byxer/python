# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

lst = [1,1,2,4,5,6,7,7,8]
lst2 = [x for x in lst if lst.count(x) >= 2]
plenty_lst = set(lst)
plenty_lst2 = set(lst2)
no_duble_lst = plenty_lst.difference(plenty_lst2)
print(list(no_duble_lst)) 


