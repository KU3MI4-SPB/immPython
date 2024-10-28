def rock_paper_scissors():
    player = int(input('1 -камень, 2 - ножницы, 3 - бумага. Введите ваш выбор: '))
    computer = 1

    if player == computer:
        print('Ничья!')
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print('Вы победили!')
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print('Вы проиграли!')
    else:
        print('Введено неверное число. Пожалуйста, введите число от 1 до 3.')

def guess_the_number():
    number = 7

    while True:
        guess_num = int(input('Введите число: '))

        if guess_num > number:
            print('Загаданное число меньше')
        elif guess_num < number:
            print('Загаданное число больше')
        elif guess_num == number:
            print('Вы угадали!')
            break

def main_menu():
    while True:
        print('Во что хотите поиграть?')
        print('1 - Камень-ножницы-бумага')
        print('2 - Угадай число')
        print('3 - Выход')

        choice = int(input('Выберите пункт меню: '))

        if choice == 1:
            rock_paper_scissors()
        elif choice == 2:
            guess_the_number()
        elif choice == 3:
            print('Выход из игры')
            break
        else:
            print('Введено неверное число. Пожалуйста, введите число от 1 до 3.')

main_menu()
