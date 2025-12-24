
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