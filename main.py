from catalog import Catalog
from menu import Menu
from storage import load, save
from utils import * 

if __name__ == "__main__":
    catalog = Catalog()
    load(catalog)

    while True:
        Menu()
        command = input("Choice command: ")

        if command == "1":
            name = input("Введите название товара: ").strip()
            if check_string(name) == False:
                name = input("Введите название товара: ").strip()
            price = float(input("Введите цену: "))
            if check_number(price) == False:
                price = float(input("Введите цену: "))
            #try:
            #    price = float(input1("Введите цену: "))
            #except ValueError:
            #    print("Цена должна быть числом")
            #    continue

            catalog.add_item(name, price)
            save(catalog)
        
        elif command == "2":
            catalog.show_items()
        elif command == "3":
            total = catalog.total_price()
            print(f"Total value = {total:.2f}")
        elif command == "4":
            name = input("Введите удаляемый товар -- ").strip()
            catalog.remove(name)
            save(catalog)
        elif command == "5":
            name = input("Введите название товара для поиска ==> ").strip()
            result = catalog.find(name) 
            if not name:
                print("Название не может быть пустым")
                continue  # ⬅ Используем continue вместо return
    
            if result is not None:
                print(f"Найден товар: {name} - {result:.2f}")
            else:
                print("Товар не найден")
            

        elif command == "6":
            name = input("Введите обновляемый товар -- ").strip()
            try:
                new_price = float(input("Введите новую цену: "))
            except ValueError:
                print("Введите число")
                continue
            catalog.update(name,new_price)
            save(catalog)
        elif command == "0":
            save(catalog)
            print("++Exit progamm++")
            break
        else:
            print("__Wrong command__")
