numbers = [int(x) for x in input('Введите числа через пробел: ').split()]
max_numbers = numbers[0]

for num in numbers:
    if num > max_numbers:
        max_numbers = num

print(max_numbers)