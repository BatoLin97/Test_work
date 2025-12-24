def check_string(data: str) -> bool:      
    """
    Docstring для check_string
    
    :param data: делает проверку на пустую строку, и если строка не пустая, то возвращает True
    :return: True или False
    :rtype: bool    
    """      
    if not data.strip():
        print("Название не может быть пустым")
        return False
    else:
        return True
    
def check_number(number) -> bool:
    """
    Docstring для check_number
    
    :param number: делает проверку на ввод числа и является ли это числом 
    :return: True или False
    :rtype: bool
    """
    try:
        number = float(number)
        if number <= 0.0:
            print("Цена не должна быть меньше 0 ")
            return False
        else:
            return True
    except (ValueError,TypeError):
        print("Введите число")
        return False