# year = int(input('Введите год:'))
# result = True
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         result = False
# else:
#     result = False
#
# print(result)

MAX_NUMBER = 1000
MIN_NUMBER = 0
TENS = 10
HUNDREDS = 100

while True:
    number = int(input('Введите число от 1 до 999:'))
    if MIN_NUMBER < number < MAX_NUMBER:
        if number < TENS:
            result = number**2
            
