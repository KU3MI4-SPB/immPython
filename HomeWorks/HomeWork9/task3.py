from functools import wraps
from typing import Callable, Any, Optional


def counter(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f"Функцию '{func.__name__}' вызвали {wrapper.count} раз")
        return result

    wrapper.count = 0
    return wrapper


@counter
def greeting(name: str, age: Optional[int] = None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


@counter
def greeting2(name: str) -> None:
    print(f'Привет, {name}!')


def main() -> None:
    greeting("Том")
    greeting("Миша", age=100)
    greeting2("Маша")
    greeting(name="Катя", age=16)


main()
