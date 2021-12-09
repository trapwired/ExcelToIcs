import pandas as pd
import os
import workday
from icalendar import Calendar, Event
import pytz
from datetime import datetime

SHEET_NAME = 'Februar'
NAME = 'Carla'
HOLIDAYS = ['x', 'F']
YEAR = 2022

def start():
    wd_dict = init_workdays()

    for file in os.listdir('excel'):
        if file.endswith('.xlsx'):
            excel_path = os.path.join('excel', file)
            break # we only use the first excel we find

    df = pd.read_excel(excel_path, sheet_name=SHEET_NAME)
    dates = None
    workdays = None
    for row in range(df.shape[0]):
        line = ''
        for col in range(df.shape[1]):
            line += str(df.iat[row, col]) + '|'
        if '15|16|17|18' in line and dates is None:
            dates = df.loc[row]
        elif NAME in line and workdays is None:
            workdays = df.loc[row]

    print(NAME)
    cal = Calendar()
    tz = pytz.timezone('Europe/Zurich')
    month = get_month(SHEET_NAME)
    for i in range(dates.shape[0]):
        date = dates.iat[i]
        if not pd.isna(date):
            wd = workdays.iat[i]
            if not pd.isna(wd):
                wd = str(wd).strip()
                if wd in wd_dict.keys():
                    wd_shift = wd_dict[wd]
                    day = dates.iat[i]

                    print(f"{day}.{SHEET_NAME}: {wd_shift.id} ({wd_shift.start}, {wd_shift.end})")

                    event = Event()
                    event.add('summary', wd_shift.get_name())
                    event.add('dtstart', datetime(YEAR, month, day, wd_shift.h_start, wd_shift.m_start, 0, tzinfo=tz))
                    if workday.is_nightshift(wd_shift):
                        event.add('dtend', datetime(YEAR, month, day + 1, wd_shift.h_end, wd_shift.m_end, 0, tzinfo=tz))
                    else:
                        event.add('dtend', datetime(YEAR, month, day, wd_shift.h_end, wd_shift.m_end, 0, tzinfo=tz))

                    # event.add('dtstamp', datetime(YEAR, month, 4, 0, 10, 0, tzinfo=pytz.utc))
                    cal.add_component(event)
                else:
                    if wd not in HOLIDAYS:
                        print('Unknown Shift: ' + wd)
    export = os.path.join('export', f"export_{SHEET_NAME}_{NAME}.ics")
    with open(export, 'wb') as f:
        f.write(cal.to_ical())

def init_workdays():
    res = dict()
    wd_list = workday.getWorkDays()
    for wd in wd_list:
        res[wd.id] = wd
    return res

def get_month(month: str):
    month_dict = dict()
    month_dict['Januar'] = 1
    month_dict['Februar'] = 2
    month_dict['März'] = 3
    month_dict['April'] = 4
    month_dict['Mai'] = 5
    month_dict['Juni'] = 6
    month_dict['Juli'] = 7
    month_dict['August'] = 8
    month_dict['September'] = 9
    month_dict['Oktober'] = 10
    month_dict['November'] = 11
    month_dict['Dezember'] = 12
    return month_dict[month]


if __name__ == '__main__':
    start()
