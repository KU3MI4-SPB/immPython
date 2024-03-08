from fractions import Fraction


def calculate_fractions(frac1, frac2):
    # Преобразуем строки в экземпляры Fraction
    fraction1 = Fraction(frac1)
    fraction2 = Fraction(frac2)

    # Вычисляем сумму и произведение
    sum_result = fraction1 + fraction2
    product_result = fraction1 * fraction2

    # Преобразуем результаты обратно в строки
    sum_str = f"{sum_result.numerator}/{sum_result.denominator}"
    product_str = f"{product_result.numerator}/{product_result.denominator}"

    # Возвращаем результаты
    return f"Сумма дробей: {sum_str}\nПроизведение дробей: {product_str}"


# Тестируем функцию
frac1 = "1/2"
frac2 = "1/3"
result = calculate_fractions(frac1, frac2)
print(result)
print(result)