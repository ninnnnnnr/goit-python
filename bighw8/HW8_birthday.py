import datetime


def congratulate(users):
    dict_us = {}
    monday = datetime.date.today() + datetime.timedelta(days=8 - datetime.datetime.today().isoweekday())

    for user in users:
        b_day = user.get('birthday')
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        wd_day = monday + datetime.timedelta(days=4)
        if monday <= b_day.date() <= wd_day:
            dd = week_days[b_day.weekday()]
            dict_us.setdefault(dd, []).append(user.get('name'))

        weekend_date = monday - b_day.date()
        if weekend_date.days == 1 or weekend_date.days == 2:
            dict_us.setdefault(week_days[0], []).append(user.get('name'))

    for key, value in dict_us.items():
        names = ', '.join(value)
        print('{0}: {1}'.format(key, names))


users = [
        {'name': 'Nik1', 'birthday': datetime.datetime(year=2021, month=8, day=16)},
        {'name': 'Nik2', 'birthday': datetime.datetime(year=2021, month=8, day=16)},
        {'name': 'Nik3', 'birthday': datetime.datetime(year=2021, month=8, day=17)},
        {'name': 'Nik4', 'birthday': datetime.datetime(year=2021, month=8, day=18)},
        {'name': 'Nik5', 'birthday': datetime.datetime(year=2021, month=8, day=18)},
    ]

congratulate(users)
