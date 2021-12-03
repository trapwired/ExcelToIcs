import pandas as pd
import os
import workday

SHEET_NAME = 'Februar'
NAME = 'Carla'
HOLIDAYS = ['x', 'F']

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
    for i in range(dates.shape[0]):
        date = dates.iat[i]
        if not pd.isna(date):
            wd = workdays.iat[i]
            if not pd.isna(wd):
                wd = str(wd).strip()
                if wd in wd_dict.keys():
                    wd_shift = wd_dict[wd]
                    print(f"{dates.iat[i]}.{SHEET_NAME}: {wd_shift.id} ({wd_shift.start}, {wd_shift.end})")
                else:
                    if wd not in HOLIDAYS:
                        print('Unknown Shift: ' + wd)

def init_workdays():
    res = dict()
    wd_list = workday.getWorkDays()
    for wd in wd_list:
        res[wd.id] = wd
    return res


if __name__ == '__main__':
    start()
