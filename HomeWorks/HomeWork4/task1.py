def digits_summ(num):
    summ = 0
    while num > 0:
        digit = num % 10
        summ += digit
        num //= 10
    print('Сумма цифр', summ)

def max_digits(num):
    max_digit = 0
    while num > 0:
        digit = num % 10
        if digit > max_digit:
            max_digit = digit
        num //= 10
    print('Максимальная цифра', max_digit)

def min_digits(num):
    min_digit = 10
    while num > 0:
        digit = num % 10
        if digit < min_digit:
            min_digit = digit
        num //= 10
    print('Минимальная цифра', min_digit)

while True:
    num = int(input('Введите число: '))
    action = int(input('Введите номер действия: 1 - сумма цифр, 2 - максимальная цифра, 3 - минимальная цифра'))

    if action == 1:
        digits_summ(num)
    elif action == 2:
        max_digits(num)
    elif action == 3:
        min_digits(num)
    else:
        print('Неверное действие. Повторите ввод.')