def max_of_2(number_1, number_2):
    if number_1 > number_2:
        return number_1
    else:
        return number_2

def max_of_3(number_1, number_2, number_3):
    return max_of_2(max_of_2(number_1, number_1), number_3)

digit1 = int(input('Введите первое число: '))
digit2 = int(input('Введите второе число: '))
digit3 = int(input('Введите третье число: '))

print(f'Максимальное число из {digit1}, {digit2} и {digit3} - {max_of_3(digit1, digit2, digit3)}')