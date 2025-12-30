class Catalog:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if not name:
            print("Название не может быть пустым")
            return
        if not isinstance(price, (int, float)) or price <= 0:
            print("Цена должна быть числом больше 0")
            return

        if name in self.items:
            print("Товар уже существует")
            return
        
        self.items[name] = price
        print("✔ Товар добавлен")

    def show_items(self):
        if not self.items:
            print("Каталог пуст")
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
        if not isinstance(new_price, (int, float)):
            print("Цена должна быть числом")
            return False
        if name not in self.items:
            print("Товар не найден")
            return False
        
        self.items[name] = new_price
        return True


    def find(self,name):
        return self.items.get(name)

    def clear(self):
        self.items.clear()
        print("Каталог очищен") 

    