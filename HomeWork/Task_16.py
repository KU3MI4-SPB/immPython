def is_attacking(q1, q2):
    # Проверка, бьют ли ферзи друг друга по вертикали, горизонтали или диагоналям
    if q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return True
    return False

def check_queens(queens):
    # Проверка всех возможных пар ферзей
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True

print(check_queens(queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]))
