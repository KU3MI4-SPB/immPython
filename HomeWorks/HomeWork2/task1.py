a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

while b:
    a, b = b, a % b

print('НОД:', a)