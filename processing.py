import datetime
import pandas as pd

def readData(filename):
    print("yes")

    csvfile = pd.read_csv('files/'+filename)

    # Delete useless columns
    csvfile = csvfile.drop(['sna','sarea','ar','sareaen','snaen','aren','lat','lng'], axis=1)

    # Convert mday's type from object to datetime
    csvfile['mday'] = csvfile['mday'].astype('datetime64[ns]')

    # Sort by datetime
    csvfile = csvfile.sort_values("mday")


    for sno in range(1, 4):
    # for sno in range(1,csvfile['sno'].max()):

        filter1 = csvfile['sno'] == sno
        timeDict = timeDict_creator('2018-03-01 00:00:00', '2018-03-31 23:00:00')

        # for row in csvfile.itertuples():
        for tkey, tvalue in timeDict.items():
            # print('k:{0}, v:{1}'.format(tkey,tvalue))

            filter2 = csvfile['mday'].between(tkey, datetime.datetime.strptime(tkey, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=1))

            # filtered_csvfile is filtered by "location"sno & "time"mday
            filtered_csvfile = csvfile[(filter1 & filter2)]
            count = filtered_csvfile.shape[0]
            print('****************************')
            print(filtered_csvfile)

            quantity = 0
            for row in filtered_csvfile.itertuples():
                lendout = row[2] - row[3]
                quantity = quantity + lendout

            if quantity == 0 or count == 0:
                average = 0
            else:
                average = round(quantity / count, 2)

            print('average is {0}'.format(average))
            timeDict[tkey] = average
            # if row[1] == sno:
            #     # print(type(row[4]))
            #     # print(row[4])
            #     t = row[4].to_pydatetime()
            #     # print(type(row[4]))
            #     string_t = t.strftime("%Y-%m-%d %H:%M:%S")
            #     print(string_t[:16])
            #     # print(row[4].hour, row[4].minute)
            #
            #     siteDict.append(timeDict)
            #     # string_t = row[4]
            #     # t = datetime.datetime.fromtimestamp(row[4])
            #     # print(t)
        # print(timeDict)
        siteDict[sno] = timeDict
        # print(siteDict)


def timeDict_creator(String_startTime, String_endTime):

    # *** set initial values
    timeDict = {}

    Date_startTime = datetime.datetime.strptime(String_startTime, "%Y-%m-%d %H:%M:%S")
    next_Date_startTime = Date_startTime + datetime.timedelta(hours=1)
    next_String_startTime = next_Date_startTime.strftime("%Y-%m-%d %H:%M:%S")

    timeDict[String_startTime] = 0

    while next_String_startTime <= String_endTime:
        timeDict[next_String_startTime] = 0
        next_Date_startTime = datetime.datetime.strptime(next_String_startTime, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=1)
        next_String_startTime = next_Date_startTime.strftime("%Y-%m-%d %H:%M:%S")

    return timeDict

siteDict = {}

readData('export.csv')

print(siteDict[1])
print(siteDict[2])
print(siteDict[3])


