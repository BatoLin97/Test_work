class Catalog:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if not name:
            print("Название не может быть пустым")
            return
        
        if name in self.items:
            print("Товар уже существует")
            return
        """try:
            #price = float(input("Введите цену: "))
            if price <= 0:
                print("Цена должна быть больше нуля")
                return
        except ValueError:
            print("Цена должна быть числом")
            return"""
        self.items[name] = price
        print("✔ Товар добавлен")

    def show_items(self):
        if not self.items:
            print("Empty Catalog")
            return
        for name, price in self.items.items():
            print(f"- {name}: {price:.2f}")
    
    def total_price(self):
        return sum(self.items.values())

    def remove(self,name):
        if not name:
            print("Название не может быть пустым")
            return
        if name in self.items:
            self.items.pop(name)
            print("Товар удален")
        else:
            print("Товара нет в списке")
            return
    
    def update(self,name,new_price)-> bool:
        if not name:
            print("Название не может быть пустым")
            return False
        if name not in self.items:
            print("Товар не найден")
            return False
        try:
            if new_price <= 0:
                print("Цена не должна быть меньше 0 ")
                return False
        except ValueError:
            print("Введите число")
            return False
        self.items[name] = new_price
        return True


    def find(self,name):
        return self.items.get(name)


""" 
    def save(self):
        with open ("catalog_1.txt", "w", encoding="utf-8") as file:
            for name, price in self.items.items():
                file.write(f"{name}:{price}\n")
    
    def load(self):
        try:
            with open("catalog_1.txt","r", encoding="utf-8") as file:
                for line in file:
                    name, price = line.strip().split(":")
                    self.items[name] = float(price)
        except FileNotFoundError:
            pass
"""

"""
        if not name:
            print("Название не может быть пустым")
            return

        if name in self.items:
            return name, self.items[name]
        else:
            return("Товар не найден")
"""        
