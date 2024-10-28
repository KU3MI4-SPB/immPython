import random
import string

length = int(input('Введите длину пароля: '))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))

print('Ваш пароль:', password)