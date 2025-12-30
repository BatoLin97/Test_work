class Storage:
    File_Name = "catalog.txt"

    @staticmethod
    def save(items: dict) -> None:
        with open (Storage.File_Name, "w", encoding="utf-8") as file:
            for name, price in items.items():
                file.write(f"{name}:{price}\n")

    @staticmethod
    def load() -> dict:
        items = {}
        try:
            with open(Storage.File_Name,"r", encoding="utf-8") as file:
                for line in file:
                    try:
                        name, price = line.strip().split(":")
                        items[name] = float(price)
                    except ValueError:
                        continue
        except FileNotFoundError:
            print("Файл не найден, создан новый каталог")
        
        return items
    
    