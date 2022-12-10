from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):

    weekdays = {0: 'Monday', 1: 'Tuesday',
                2: 'Wednesday', 3: 'Thursday', 4: 'Friday'}
    current_date = datetime.now().date()
    birthdays = defaultdict(list)

    for user in users:
        for name, birthday in user.items():
            user_birthdate = datetime.date(birthday).replace(year=2022)
            if current_date <= user_birthdate < current_date + timedelta(days=7):
                day_of_week = user_birthdate.weekday()
                if day_of_week == 5:
                    birthdays[user_birthdate + timedelta(days=2)].append(name)
                elif day_of_week == 6:
                    birthdays[user_birthdate + timedelta(days=1)].append(name)
                else:
                    birthdays[user_birthdate].append(name)
            else:
                continue

    if birthdays:
        for day in sorted(birthdays):
            print(f"{weekdays[day.weekday()]}: {', '.join(birthdays[day])}")
    else:
        print('No birthdays next week')
