import random

class House:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money
    def buy_food(self, quantity, price):
        if self.money >= price:
            self.food += quantity
            self.money -= price
            print(f"Купили {quantity} единиц еды за {price} денег.")
        else:
            print("Недостаточно денег для покупки еды!")
    def earn_money(self, salary):
        self.money += salary
        print(f"Заработали {salary} денег.")


class Human:
    def __init__(self, name, house):
        self.name = name
        self.hunger = 50
        self.house = house
    def eat(self):
        if self.house.food >= 10:
            self.hunger += 10
            self.house.food -= 10
            print(f"{self.name} поел. Сытость увеличилась до {self.hunger}, еда уменьшилась до {self.house.food}.")
        else:
            print(f"{self.name} хотел поесть, но в доме недостаточно еды!")
    def work(self):
        self.hunger -= 10
        self.house.earn_money(50)
        print(f"{self.name} поработал. Сытость уменьшилась до {self.hunger}.")
    def play(self):
        self.hunger -= 5
        print(f"{self.name} поиграл. Сытость уменьшилась до {self.hunger}.")
    def shop_for_food(self):
        self.house.buy_food(15, 50)
    def live_day(self):
        cube = random.randint(1, 6)
        print(f"\nСегодняшний кубик: {cube}")
        if self.hunger < 20:
            self.eat()
        elif self.house.food < 10:
            self.shop_for_food()
        elif self.house.money < 50:
            self.work()
        elif cube == 1:
            self.work()
        elif cube == 2:
            self.eat()
        else:
            self.play()

        if self.hunger <= 0:
            print(f"{self.name} умер от голода.")
            return False
        return True


house1 = House()
human1 = Human("Артем", house1)
human2 = Human("Даша", house1)
house2 = House()
human3 = Human("Филипп", house2)
try:
    for day in range(1, 366):
        print(f"\nДень {day}")
        if not human1.live_day() or not human2.live_day() or not human3.live_day():
            print(f"Человек умер на {day} день.")
            break

finally:
    print("\nСостояние пары:")
    print(f"Еда в холодильнике - {house1.food}, Деньги - {house1.money}")
    print(f"Состояние {human1.name}: Сытость - {human1.hunger}")
    print(f"Состояние {human2.name}: Сытость - {human2.hunger}\n")
    print("Состояние одиночки:")
    print(f"Еда в холодильнике - {house2.food}, Деньги - {house2.money}")
    print(f"Состояние {human3.name}: Сытость - {human3.hunger}")