from fractions import Fraction

frac1 = input('Введите первую дробь (a/b):' )
frac2 = input('Введите вторую дробь (c/d):' )

numerator1, denominator1 = map(int, frac1.split('/'))
numerator2, denominator2 = map(int, frac2.split('/'))

f1 = Fraction(numerator1, denominator1)
f2 = Fraction(numerator2, denominator2)

sum_frac = f1 + f2
product_frac = f1 * f2

print(f'Сумма дробей: {sum_frac}')
print(f'Произведение дробей: {product_frac}')