import pandas as pd

def combine():

    csvfile03 = pd.read_csv('final_files/' + 'siteDictAll_March_new 08192019_csv.csv')
    print(type(csvfile03))
    csvfile04 = pd.read_csv('final_files/' + 'siteDictAll_April_new 08192019v3_csv.csv')
    print(type(csvfile04))

    print(csvfile03.head())
    print(csvfile04.head())

    frames = [csvfile03, csvfile04]

    result = pd.concat(frames)

    print(type(result))
    # print(result)

    result.to_excel('final_files/siteDictAll.xlsx', sheet_name='ubike_Station_stats', index=False)

def open():

    csvfile = pd.read_excel('final_files/' + 'siteDictAll.xlsx')
    print(csvfile)



# combine()

open()