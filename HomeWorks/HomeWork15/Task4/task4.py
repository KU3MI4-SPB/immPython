import argparse


def main():
    parser = argparse.ArgumentParser(description='Обработка чисел и строк.')
    parser.add_argument('number', type=int, help='Целое число')
    parser.add_argument('text', type=str, help='Строка для обработки')
    parser.add_argument('--verbose', action='store_true', help='Включить дополнительный вывод')
    parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')
    args = parser.parse_args()
    if args.verbose:
        print(f'Обрабатываем число: {args.number}')
        print(f'Обрабатываем текст: "{args.text}"')
        print(f'Количество повторений: {args.repeat}')
    result = (args.text + ' ') * args.repeat
    print(f'Результат: {result.strip()}')


if __name__ == '__main__':
    main()

# python task4.py 7 "Aksai" --verbose --repeat 7

# Обрабатываем число: 5
# Обрабатываем текст: "Aksai"
# Количество повторений: 7
# Результат: Aksai Aksai Aksai Aksai Aksai Aksai Aksai

