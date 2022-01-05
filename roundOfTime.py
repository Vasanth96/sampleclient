import pandas as pd
import datetime

# dt = datetime.datetime(2012,12,31,23,55,59)
print(datetimeobj)


def rounder(t):
    if t.minute >= 0 and t.minute < 7:
        return t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
    elif t.minute >= 7 and t.minute < 20:
        return t.replace(second=0, microsecond=0, minute=15, hour=t.hour)
    elif t.minute >= 20 and t.minute < 40:
        return t.replace(second=0, microsecond=0, minute=30, hour=t.hour)
    elif t.minute >= 40 and t.minute < 50:
        return t.replace(second=0, microsecond=0, minute=45, hour=t.hour)
    elif t.minute >= 50:
        if(t.hour == 23):
            tdelta = datetime.timedelta(hours=1)
            t = t+tdelta
            return t.replace(second=0, microsecond=0, minute=00, hour=00)
        else:
            return t.replace(second=0, microsecond=0, minute=00, hour=t.hour+1)


        # 2018-02-22 22:03:53.831589
df = pd.read_excel('/Users/vasanth/Downloads/CIB_AHU.L01.1-N-1-1.xlsx')

for ind, row in df.iterrows():
    strdate = row['time']
    dt_tuple = tuple([int(x) for x in strdate[:10].split('-')])+tuple([int(x)
                                                                       for x in strdate[11:19].split(':')])+tuple([int(x) for x in strdate[20:26].split('.')])
    datetimeobj = datetime.datetime(
        dt_tuple[0], dt_tuple[1], dt_tuple[2], dt_tuple[3], dt_tuple[4], dt_tuple[5], dt_tuple[6])
    df.loc[ind, "Actual time"] = str(rounder(datetimeobj))
# 2018-02-22 22:00:00.000000
