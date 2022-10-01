from datetime import datetime, date
from collections import defaultdict


week = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

users = [
    {'name': 'Sem', 'birthday': datetime(year=1999, month=9, day=24)},
    {'name': 'Din', 'birthday': datetime(year=1998, month=9, day=27)},
    {'name': 'Bob', 'birthday': datetime(year=1997, month=9, day=25)},
    {'name': 'Kas', 'birthday': datetime(year=1996, month=9, day=20)}
]


def get_birthdays_per_week(users):
    weeks_winner = dict()
    users_to_monday = defaultdict(list)
    curent_data = datetime.now()
    curent_weekend = datetime.weekday(curent_data)
    i = 0

    for user in users:
        name = user['name']
        birthday = user['birthday']

        
        birthday_rep = birthday.replace(year=curent_data.year)      
        birthday_day = datetime.weekday(birthday_rep)              # День недели
        interval = birthday_rep - curent_data
        user_day_of_week = curent_weekend + interval.days

        if (interval.days + 1) <= 0:
            continue
        
        if 0 <= user_day_of_week <= 6:
            if birthday_day in (5,6):
                users_to_monday['Monday'].append(name)
        else:
            weeks_winner[week[birthday_day]] = name
        
    return weeks_winner, users_to_monday


if __name__ =='__main__':
    get_birthdays_per_week(users)