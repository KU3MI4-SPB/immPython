class Parent:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.children = []

    def info(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет")

    def add_child(self, child):
        if self.age - child.age >= 16:
            self.children.append(child)
            print(f"Ребёнок {child.name} добавлен к {self.name}.")
        else:
            print(f"Ребёнок {child.name} не добавлен к {self.name}, так как разница в возрасте слишком мала.")

    def feed(self, child):
        if child in self.children:
            child.hungry = False
            print(f"{self.name} покормил(а) {child.name}.")
        else:
            print(f"{child.name} не является ребёнком {self.name}.")

    def calm(self, child):
        if child in self.children:
            child.calm = True
            print(f"{self.name} успокоил(а) {child.name}.")
        else:
            print(f"{child.name} не является ребёнком {self.name}.")

    def list_children(self):
        if self.children:
            print(f"У {self.name} есть следующие дети:")
            for child in self.children:
                print(f" - {child}")
        else:
            print(f"У {self.name} нет детей.")


class Child:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.calm = False
        self.hungry = True
    def get_status(self):
        calm_status = "спокоен" if self.calm else "не спокоен"
        hungry_status = "сыт" if not self.hungry else "голоден"
        print(f"Ребёнок {self.name} {calm_status} и {hungry_status}.")

    def __str__(self):
        return f"Ребёнок {self.name}, {self.age} лет"


parent = Parent("Иван", 40)
child1 = Child("Анна", 20)
child2 = Child("Петя", 10)
child3 = Child("Маша", 3)

for child in [child1, child2, child3]:
    parent.add_child(child)

parent.info()
parent.list_children()

for child in parent.children:
    parent.feed(child)
    parent.calm(child)
    child.get_status()