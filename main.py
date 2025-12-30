from catalog import Catalog
from menu import Menu
from storage import Storage
from utils import check_string, check_number

if __name__ == "__main__":
    catalog = Catalog()
    catalog.items = Storage.load()

    def save(catalog: Catalog) -> None:
        Storage.save(catalog.items)

    menu = Menu()

    while True:
        menu.show_menu()
        command = input("Choice command: ")

        if command == "1":
            name = input("Введите название товара: ").strip()
            while not check_string(name):
                print("Название не может быть пустым")
                name = input("Введите название товара: ").strip()
            while True:
                try:
                    price = float(input("Введите цену товара: "))
                    if check_number(price):
                        break
                    else:
                        print("Цена должна быть числом больше 0")
                        continue
                except ValueError:
                    print("Введите число")
            catalog.add_item(name, price)
            save(catalog)
            print("✔ Товар добавлен")
        
        elif command == "2":
            catalog.show_items()

        elif command == "3":
            total = catalog.total_price()
            print(f"Total value = {total:.2f}")
        
        elif command == "4":
            name = input("Введите удаляемый товар -- ").strip()
            while not check_string(name):
                print("Название не может быть пустым")
                name = input("Введите удаляемый товар -- ").strip()
            if catalog.remove(name):
                print(f"✔ Товар '{name}' удален")
                save(catalog)
            else:
                print("Товара нет в списке")

        elif command == "5":
            name = input("Введите название товара для поиска ==> ").strip()
            if not name:
                print("Название не может быть пустым")
                continue  # ⬅ Используем continue вместо return

            result = catalog.find(name)

            if result is not None:
                print(f"Найден товар: {name} - {result:.2f}")
            else:
                print("Товар не найден")
            

        elif command == "6":
            name = input("Введите обновляемый товар -- ").strip()
            if not name:
                print("Название не может быть пустым")
                continue
            
            if not catalog.find(name):
                print("Товар не найден")
                continue
            while True:
                try:
                    new_price = float(input("Введите новую цену: "))
                    if check_number(new_price):
                        break
                    else:
                        print("Цена должна быть числом больше 0")
                        continue
                except ValueError:
                    print("Введите число")
                    continue    
            if catalog.update(name, new_price):
                save(catalog)
                print(f"✔ Товар '{name}' обновлен")
            else:
                print("Ошибка при обновлении товара")
        elif command == "0":
            save(catalog)
            print("++Exit progamm++")
            break
        else:
            print("__Wrong command__")
        print("\n" + "="*40 + "\n")


