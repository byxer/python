def date_info():
    lst_info = []
    surname = input('Введите фамилию: ')
    lst_info.append(surname.title())
    name = input('Введите имя: ')
    lst_info.append(name.title())
    phone = ''
    valid = False
    while not valid:
        try:
            phone = input('Введите номер телефона: ')
            if len(phone) != 11:
                print('Не корректный ввод! В номере должно быть 11 цифр.')
            else:
                phone = int(phone)
                valid = True
        except:
            print('Не корректный ввод! Номер телефона должен состоять из цифр.')
    lst_info.append(phone)
    description = input('Введите описание: ')
    lst_info.append(description.title())
    return lst_info

def save_scv(lst_info):
    file = 'phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{lst_info[0]};{lst_info[1]};{lst_info[2]};{lst_info[3]}\n')

def save_txt(lst_info):
    file = 'phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {lst_info[0]}\nИмя: {lst_info[1]}\nНомер телефона: {lst_info[2]}\nОписание: {lst_info[3]}\n')