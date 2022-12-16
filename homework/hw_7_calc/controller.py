import view
import menu
import logger

def button_click():
    value_a = view.get_value()
    oper = view.get_operation()
    value_b = view.get_value()
    func = menu.model[oper]
    func.init(value_a, value_b)
    result = func.do_it()
    view.get_result(f'{value_a} {oper} {value_b} = {result}')
    logger.get_log(result, value_a, value_b, oper)