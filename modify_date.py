import pandas as pd

def read():
    df = pd.read_excel('siteDictAll_April.xlsx', dtype={'日期':str})
    return df

def modify(df):
    for row in df.itertuples():
        # print(row.時間, row.日期)
        t1 = row.日期
        # print(len(t1))
        if len(t1) == 8:
            t1_new = t1[1:]
        else:
            t1_new = t1[3] + '/' + t1[5:7] + '/' + t1[8:10]
        # print(row.時間, t1_new)
        df.at[row.Index, '日期'] = t1_new
        # print(type(t1))
        # t2 = row['日期']
        # print(t2)
        # print(type(t2))
        # if type(row.日期) != 'str':
        #     t1_1 = t1.strftime("%Y-%m-%d %H:%M:%S")
        #     print(t1_1)
        # else:

        # t1_2 = t1[1:]
        # print(t1_2)
    return df

def export(results):

    results.to_excel('siteDictAll_April_new.xlsx', sheet_name='ubike_Station_stats', index=False)
    print(results)

df = read()
results = modify(df)
export(results)