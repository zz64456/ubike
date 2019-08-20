import pandas as pd, os

def merge(folder):
    files = []
    for r, d, f in os.walk(folder):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(file))
    # for f in files:
    #     print(f)
    files.sort()
    for index in range(len(files)):
        print(files[index])

        # csvfile = pd.read_csv('April/' + filename)
        # print(csvfile)

        # temp = csvfile.values.tolist()
        # print(temp)



siteDictAll = []

target_folder = 'April'

merge((target_folder))