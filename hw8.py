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


if __name__ == "__main__":

    users = [
        {'Bill': datetime(1983, 12, 10),
         'Jill': datetime(1984, 12, 11),
         'Kim': datetime(1985, 12, 12),
         'Jan': datetime(1986, 12, 13),
         'Jack': datetime(1987, 12, 13),
         'John': datetime(1988, 12, 17)},
        {'Dave': datetime(1991, 12, 14),
         'Den': datetime(1992, 12, 15),
         'Nick': datetime(1993, 12, 16),
         'ALisa': datetime(1994, 12, 14),
         'Jim': datetime(1995, 12, 15)}
    ]

    get_birthdays_per_week(users)
