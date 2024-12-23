from datetime import datetime

now = datetime.now()
formatted_date_time = now.strftime('%Y-%m-%d %H:%M:%S')
day_of_week = now.strftime('%A')
week_number = now.isocalendar()[1]

print(f'Текущая дата и время: {formatted_date_time}')
print(f'День недели: {day_of_week}')
print(f'Номер недели в году: {week_number}')
