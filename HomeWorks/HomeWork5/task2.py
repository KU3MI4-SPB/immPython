def calculate_bonus(names, salary, bonus):
    result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
    return result

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

result = calculate_bonus(names, salary, bonus)
print(result)