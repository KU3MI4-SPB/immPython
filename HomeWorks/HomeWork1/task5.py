start = 1
finish = 100
count = 1

while True:
    n = (start + finish) // 2
    print('Заданное число равно, меньше или больше: ', n)
    answer = int(input('1 - равно, 2 - меньше, 3 - больше: '))

    if answer == 1:
        print('Я угадал! Ура! с', count, 'попытки')
        break
    elif answer == 2:
        finish = n
    elif answer == 3:
        start = n

    count += 1

