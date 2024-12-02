from functools import wraps
from time import sleep
from typing import Callable, Any


def slowdown_2s(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        sleep(2)
        result = func(*args, **kwargs)
        return result

    return wrapper


@slowdown_2s
def test() -> None:
    print('<Тут что-то происходит...>')


@slowdown_2s
def another_function() -> None:
    print('Еще один тестовый вывод.')


if __name__ == "__main__":
    test()
    another_function()
