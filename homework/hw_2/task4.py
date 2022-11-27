# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите чило n = "))
list1 = []
for i in range(-abs(n), abs(n) + 1, 1):
    list1.append(i)
print(f"Сгенерированный список: {list1}")
p = 1
data = open("file.txt", "r")
for line in data:
    if line == "":
        break
    p *= list1[int(line)]
data.close()
print(f"Произведение элементов (позиции указаны в файле file.txt) = {p}")