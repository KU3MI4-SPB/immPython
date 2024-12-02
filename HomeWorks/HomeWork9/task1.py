from functools import wraps
from typing import Callable, Any

def how_are_you(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        input('Как дела? ') # Запрашиваем ответ у пользователя
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs) # Вызов оригинальной функции
        return result
    return wrapper

@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')

@how_are_you
def another_function() -> None:
    print('Еще один тестовый вывод.')


if __name__ == "__main__":
    test()
    another_function()