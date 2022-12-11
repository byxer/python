# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('text_rle.txt', 'w') as file:
    file.write(input('Напишите текст необходимый для сжатия = '))
with open('text_rle.txt', 'r') as file:
    text = file.readline()
    text_compression = text.split()
print(f'Сжатые данные: {text}')

def rle (text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''
    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding
text_rle = rle(text)
with open('text.txt', 'w') as file:
    file.write(f'{text_rle}')
print(f'Исходные данные: {text_rle}')