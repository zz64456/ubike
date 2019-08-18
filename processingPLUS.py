import datetime, csv
import pandas as pd

def read():
    df = pd.read_excel('siteDictAll.xlsx')

    # print("Column headings:")
    # print(df.columns)

    print(df)
    for i in df.index:
        print(df['站名'][i])

read()
