from datetime import datetime as dt

def get_log(result, value_a, value_b, oper):
    dtime = dt.now()
    with open('log.txt', 'a', encoding = 'UTF - 8') as file:
        file.write('{}; Вводные данные: {} {} {}; Ответ: {}\n'.format(dtime, value_a, oper, value_b, result))
           
   