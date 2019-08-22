import pandas as pd
pd.set_option('display.max_columns', 999)


def read():
    df = pd.read_excel('final_files/siteDictAll_April_new 08192019.xlsx')
    return df

def modify(df):
    for row in df.itertuples():
        # print(row)
        # print(row.時間, type(row.時間))

        datetime_time = row.時間.to_pydatetime()
        # print(datetime_time, type(datetime_time))
        df.at[row.Index, '時間'] = datetime_time

        str_time = datetime_time.strftime("%Y/%m/%d")
        # print(str_time, type(str_time))

        # print(df.at[row.Index, '日期'])

        df.at[row.Index, '日期'] = str_time
        # print(df.at[row.Index, '日期'])


        # print(row)
        # datetime_t1 = datetime.datetime.strptime(t1, "%m/%d/%Y")

        # print(datetime_t1, type(datetime_t1))
        # print()
        # if len(t1) == 8:
        #     t1_new = t1[1:]
        # else:
        #     t1_new = t1[3] + '/' + t1[5:7] + '/' + t1[8:10]
        # df.at[row.Index, '日期'] = t1_new

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

    results.to_excel('final_files/siteDictAll_April_new 08192019v3.xlsx', sheet_name='ubike_Station_stats', index=False)
    print(results)

df = read()

results = modify(df)
# print(results)

export(results)