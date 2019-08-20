
import pandas as pd

def read():
    df = pd.read_excel('siteDictAll.xlsx', dtype={'時間':str})

    date = []
    hour = []

    for row in df.itertuples():

        d = row.時間[:10]
        t = row.時間[11:]
        date.append(d)
        hour.append(t)

    df['日期'] = date
    df['時刻'] = hour

    return df


def export(df):
    df.to_excel('siteDictAll_v2.xlsx', sheet_name='ubike_Station_stats', index=False)



cols = [3]
# dframe = read()
# print(dframe)
# export(dframe)

dt = '2018-04-01 02:00:00'
print(dt)
date = dt[5:7]+'/'+dt[8:10]+'/'+dt[2:4]
print(date)