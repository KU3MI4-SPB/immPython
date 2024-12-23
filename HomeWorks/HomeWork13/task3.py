import os
import random

MAGIC_NUMBER = 777


class MagicFileProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.file_path = self.get_file_path()
        self.magic_sum = 0

    def get_file_path(self):
        return os.path.join(os.path.abspath('.'), self.filename)

    def is_exception_raise(self):
        return random.randint(1, 13) == 7

    def pre_init(self):
        try:
            os.remove(self.file_path)
        except OSError as ex:
            print(ex)
            print('Данный файл не может быть удален')

    def process_input(self):
        try:
            input_number = int(input('Введите число: '))
            self.magic_sum += input_number
            if self.is_exception_raise():
                raise Exception('Вас постигла неудача!')
            with open(self.file_path, 'a') as out_fd:
                out_fd.write(str(input_number) + '\n')
        except (ValueError, KeyboardInterrupt) as ex:
            print(ex)
            print('Возникли проблемы при вводе.')
            print('Попробуйте еще раз')

    def run(self):
        self.pre_init()
        while self.magic_sum < MAGIC_NUMBER:
            self.process_input()
            print('Вы успешно выполнили условие для выхода из порочного цикла!')


# Запуск программы
if __name__ == "__main__":
    processor = MagicFileProcessor('out_file.txt')
    processor.run()
