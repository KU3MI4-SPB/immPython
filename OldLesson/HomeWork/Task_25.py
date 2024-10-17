class LotteryGame:
    def __init__(self, ticket_numbers, lottery_numbers):
        self.ticket_numbers = ticket_numbers
        self.lottery_numbers = lottery_numbers

    def compare_lists(self):
        matching_numbers = set(self.ticket_numbers) & set(self.lottery_numbers)

        if matching_numbers:
            sorted_matches = [num for num in self.ticket_numbers if num in matching_numbers]
            print(f"Совпадающие числа: {sorted_matches}")
            print(f"Количество совпадающих чисел: {len(sorted_matches)}")
        else:
            print("Совпадающих чисел нет.")


list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
game.compare_lists()

