def are_queens_safe(positions):
    def is_under_attack(row, col):
        for i in range(8):
            if i != row:
                if (positions[i][1] == col or abs(positions[i][0] - row) == abs(positions[i][1] - col)):
                    return True
        return False

    for i in range(8):
        if is_under_attack(positions[i][0], positions[i][1]):
            return False
    return True

def generate_random_queens_placement():
    import random
    return [(i, random.randint(1, 8)) for i in range(8)]

def print_valid_placements(num_placements=4):
    count = 0
    while count < num_placements:
        placement = generate_random_queens_placement()
    if are_queens_safe(placement):
        print(placement)
    count += 1


import sys
import chess
if len(sys.argv) != 9:
    print("Usage: python main.py row1 col1 row2 col2 ... row8 col8")
    sys.exit(1)

positions = [(int(sys.argv[i]), int(sys.argv[i+1])) for i in range(1, len(sys.argv), 2)]
if chess.are_queens_safe(positions):
    print("True")
else:
    print("False")