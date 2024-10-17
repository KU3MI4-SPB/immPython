a = float(input('Введите сторону a: '))
b = float(input('Введите сторону b: '))
c = float(input('Введите сторону c: '))

if a + b > c and a + c > b and b + c > a:
    print('Треугольник существует')
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or b == c or c == a:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')

else:
    print('Треугольника не существует')

