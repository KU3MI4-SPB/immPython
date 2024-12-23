import random

NIRVANA_KARMA = 500


class KillError(Exception):
    def __init__(self):
        super().__init__("Убийство. Вы и убили-с!")


class DrunkError(Exception):
    def __init__(self):
        super().__init__("Пьянство. Пьянству бой!")


class CarCrashError(Exception):
    def __init__(self):
        super().__init__("Вы попали в аварию. Стоит следить за дорогой.")


class GluttonyError(Exception):
    def __init__(self):
        super().__init__("Вы обожрались. Следует сократить порции.")


class DepressionError(Exception):
    def __init__(self):
        super().__init__("На вас напала хандра. Уныние - грех.")


def one_day():
    day_karma = random.randint(1, 7)
    if random.randint(1, 10) == 5:
        exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
        raise exception
    return day_karma


def main():
    karma = 0
    with open('karma.log', 'w', encoding='utf-8') as fl_logger:
        while True:
            try:
                karma += one_day()
            except Exception as ex:
                fl_logger.write(f'{ex}\n')
            if karma >= NIRVANA_KARMA:
                break


print('Вы достигли Нирваны! ')
print('Омм ')

if __name__ == "__main__":
    main()
