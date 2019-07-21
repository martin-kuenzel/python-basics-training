#!/usr/bin/python3
import datetime

date_today = datetime.date.today()
date_0 = datetime.date(2018,5,15)
date_1 = datetime.time(9,23,30,100000)
date_2 = datetime.datetime(2019,2,25,17,29,20,100000)

print(f'''
date_0 = {date_0}
date_today = {date_today}
date_1 = {date_1}
date_2 = {date_2}

['Mo','Di','Mi','Do','Fr','Sa','So'][date_today.weekday()] = {['Mo','Di','Mi','Do','Fr','Sa','So'][date_today.weekday()]}

date_today.strftime('%a, %d.%m.%Y') = {date_today.strftime('%a, %d.%m.%Y')}
datetime.datetime.now().strftime('%a, %d.%m.%Y') = {datetime.datetime.now().strftime('%a, %d.%m.%Y')}

date_today + datetime.timedelta(days=2) = {date_today + datetime.timedelta(days=2)}
date_today - datetime.timedelta(days=2) = {date_today - datetime.timedelta(days=2)}
date_today-date_0 = {date_today-date_0}
datetime.timedelta(days=2).days = {datetime.timedelta(days=2).days}
datetime.timedelta(days=2).total_seconds() = {datetime.timedelta(days=2).total_seconds()}
date_2 + datetime.timedelta(hours=20) = {date_2 + datetime.timedelta(hours=20)}

_-==[ Current local datetime (microsecond differences are due to execution times) ]==-_
Current local datetime datetime.datetime.today() = {datetime.datetime.today()}
Current local datetime datetime.datetime.now() = {datetime.datetime.now()} (timezone can optionally be added)
    datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=10))) = {datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=10)))}
Current local datetime datetime.datetime.utcnow() = {datetime.datetime.utcnow()} (universal time code)
''')


print("Using package pytz")
import pytz
print(f'''
datetime.datetime(2015,4,12,12,5,5, tzinfo=pytz.UTC) = {datetime.datetime(2015,4,12,12,5,5, tzinfo=pytz.UTC)}

datetime.datetime.now(tz=pytz.UTC) = {datetime.datetime.now(tz=pytz.UTC)}
this might also be used:
datetime.datetime.utcnow().replace(tzinfo=pytz.UTC) = {datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)}

datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Europe/Berlin')) = {datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Europe/Berlin'))}
datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Australia/Melbourne')) = {datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Australia/Melbourne'))}
''')

## PRINT ALL TIMEZONES WITH CURRENT DATETIME
for tz in pytz.all_timezones:
    print(f'''datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('{tz}')) = {datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone(tz))}''')

print( f'''
date_2.astimezone(pytz.timezone('Zulu')) = {date_2.astimezone( pytz.timezone('Zulu') )}
pytz.timezone('Pacific/Tahiti').localize(datetime.datetime.utcnow()) = { pytz.timezone('Pacific/Tahiti').localize(datetime.datetime.utcnow())}

datetime.datetime.now().isoformat() = {datetime.datetime.now().isoformat()}
datetime.datetime.now().strftime('%F') = {datetime.datetime.now().strftime('%F')}
datetime.datetime.now().strftime('%c') = {datetime.datetime.now().strftime('%c')}
datetime.datetime.now().strftime('%s') = {datetime.datetime.now().strftime('%s')}

datetime.datetime.now().strftime('%s') = {datetime.datetime.now().strftime('%s')}

datetime.datetime.strptime('2025/03/05', '%Y/%m/%d').strftime('%B, %d.%m.%Y') = {datetime.datetime.strptime('2025/03/05', '%Y/%m/%d').strftime('%B, %d.%m.%Y')}
''')