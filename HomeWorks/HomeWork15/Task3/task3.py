from datetime import datetime, timedelta


def get_future_date(days_from_now):
    current_date = datetime.now()
    fut_date = current_date + timedelta(days=days_from_now)
    formatted_future_date = fut_date.strftime('%Y-%m-%d')
    return formatted_future_date


days = 8
future_date = get_future_date(days)
print(f'Дата через {days} дней: {future_date}')
