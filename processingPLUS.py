
import pandas as pd

def read():
    df = pd.read_excel('siteDictAll-part1.xlsx', skiprows=1, dtype={'時間':str})

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


def output(df):
    df.to_excel('testing.xlsx', sheet_name='ubike_Station_stats', index=False)



cols = [3]
dframe = read()
output(dframe)
