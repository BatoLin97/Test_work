def check_string(data: str) -> bool:      
    """
    Docstring для check_string
    
    :param data: делает проверку на пустую строку, и если строка не пустая, то возвращает True
    :return: True или False
    :rtype: bool    
    """      
    return bool(data and data.strip())
    
def check_number(number) -> bool:
    """
    Docstring для check_number
    
    :param number: делает проверку на ввод числа и является ли это числом 
    :return: True или False
    :rtype: bool
    """
    try:
        number = float(number)
        return number > 0
    except (ValueError,TypeError):
        print("Введите число")
        return False