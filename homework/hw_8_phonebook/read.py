def read_file (file):
    with open(file, 'r', encoding='utf-8') as data:
        sp = data.read()
    return sp