# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# #Старое решение
# nums = [22, 35, 47, 65, 32]
# max = nums[0]
# for i in range(1, len(nums)):
#     if nums[i] > max:
#         max = nums[i]
# print(f"max = {max}")

#Новое решение
numbers = [22, 35, 47, 65, 32]
print (max(numbers))
print (min(numbers))