from datetime import datetime

class MyStr(str):
    def __new__(cls, value, author):
        instance = str.__new__(cls, value)
        instance.author = author
        instance.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return instance

    def __str__(self):
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {self.time})"

    def __repr__(self):
        return f"MyStr('{self}', '{self.author}')"

# Пример использования
# event = MyStr("Завершилось тестирование", "John")
# print(event)
#
# my_string = MyStr("Пример текста", "Иван")
# print(my_string)

my_string = MyStr("Мама мыла раму", "Маршак")
print(repr(my_string))



