class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        raise NotImplementedError("Подклассы должны реализовывать этот метод")

    def __str__(self):
        return f"{self.__class__.__name__} имя {self.name}"


class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Гав!"

    def __str__(self):
        return f"{super().__str__()} породы {self.breed}"


class Cat(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color

    def speak(self):
        return "Мяу!"

    def __str__(self):
        return f"{super().__str__()} цвета {self.color}"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str, *args) -> Animal:
        animal_classes = {
            'Собака': Dog,
            'Кошка': Cat
        }
        if animal_type in animal_classes:
            return animal_classes[animal_type](*args)
        else:
            raise ValueError(f"Неизвестное животное: {animal_type}")


dog = AnimalFactory.create_animal('Собака', 'Аксай', 'Тайский Риджбек')
cat = AnimalFactory.create_animal('Кошка', 'Центик', 'голубая')

print(dog)
print(dog.speak())
print(cat)
print(cat.speak())
