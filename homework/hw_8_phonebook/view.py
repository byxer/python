from record import save_scv, save_txt, date_info
from read import read_file

def menu():
    menu_sp = input('\nДля работы со справочником наберите = 1\nЗавершить работу наберите = 2\nВведите 1 или 2 = ')
    while (menu_sp == '1'):
        choice = input('\nВнести новые данные в справочник, наберите = 1\nПосмотр справочника, наберите = 2\nВведите 1 или 2 = ')
        if choice == '1':
            record_info()
        else:
            view()
        menu_sp = input('\nДля работы со справочником наберите = 1\nЗавершить работу, наберите = 2\nВведите 1 или 2 = ')
    print('\nРабота со справочником завершена.')

def view():
    print(read_file('phonebook.txt'))

def record_info():
    info = date_info()
    save_scv(info)
    save_txt(info)