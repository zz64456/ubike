import datetime, csv
import pandas as pd

# The flow :
# 1. readData() read export.csv which includes all data from government database and results an csv file "siteInfo.csv" created by export_siteInfo()
#       and a dict variable "csvfile"
# 2. put "csvfile" into average_computing() to compute amount of bike used each hour at each station, then we put results into siteDict{}

def readData(filename):
    print("Start reading...")

    csvfile = pd.read_csv('files/'+filename)

    for sno in range(1, csvfile['sno'].max()):
        filter1 = csvfile['sno'] == sno
        filtered_csvfile = csvfile[filter1]
        # print(filtered_csvfile[['sno','sna','lat','lng']])
        for row in filtered_csvfile.itertuples():
            dict = {'sna':row[7], 'lat':row[9], 'lng':row[10]}
            siteInfo_Dict[sno] = dict
            break

    # Export siteInfo to csv file
    # export_siteInfo(siteInfo_Dict)

    # Delete useless columns
    csvfile = csvfile.drop(['sna','sarea','ar','sareaen','snaen','aren','lat','lng'], axis=1)

    # Convert mday's type from object to datetime
    csvfile['mday'] = csvfile['mday'].astype('datetime64[ns]')

    # Sort by datetime
    csvfile = csvfile.sort_values("mday")

    return csvfile

def export_siteInfo(siteInfo_Dict):
    try:
        with open('siteInfo.csv', 'w', newline='') as f:
            siteInfo_columns = ['編號', '站名', '緯度', '經度']
            writer = csv.DictWriter(f, fieldnames=siteInfo_columns)
            writer.writeheader()
            for key in siteInfo_Dict.keys():
                f.write('%s' % (key))
                new_dic = siteInfo_Dict[key]
                print(new_dic)
                for insidekeys in siteInfo_Dict[key]:
                    print(new_dic[insidekeys])
                    f.write(',%s' % (new_dic[insidekeys]))
                f.write('\n')
                # for insidekeys in siteInfo[key]:
                #     f.write('%s\n' % (siteInfo[key][insidekeys]))
    except IOError:
        print("I/O error")

def average_computing(csvfile):
    # Choose site first
    for sno in range(1, 3):
    # for sno in range(1,csvfile['sno'].max()):

        # first filter to get data of a site
        filter1 = csvfile['sno'] == sno

        # create a timeDict from 2018-xx-xx 00:00 - 23:00
        timeDict = timeDict_creator('2018-03-01 00:00:00', '2018-03-31 23:00:00')

        # Put results into time interval dict
        for tkey, tvalue in timeDict.items():

            # second filter to get one site's data of each hour
            filter2 = csvfile['mday'].between(tkey, datetime.datetime.strptime(tkey,
                                                                               "%Y-%m-%d %H:%M:%S") + datetime.timedelta(
                hours=1))

            # filtered_csvfile is filtered by "location":sno & "time":mday
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

        siteDict[sno] = timeDict


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

def export_siteDict():
    try:
        with open('siteDict1-3-NewVersion.csv', 'w', newline='') as f:
            siteDict_columns = ['站名', '緯度', '經度', '時間', '借出數量']
            writer = csv.DictWriter(f, fieldnames=siteDict_columns)
            writer.writeheader()
            for key in siteDict.keys():
                for timekey in siteDict[key]:
                    f.write('%s,%s,%s,%s,%s\n' % (siteInfo_Dict[key]['sna'], siteInfo_Dict[key]['lat'], siteInfo_Dict[key]['lng'], timekey, siteDict[key][timekey]))
    except IOError:
        print("I/O error")

# Information of each site, 4 columns : site_number, site_name, site_latitude, site_longitude
siteInfo_Dict = {}

# Computed information of amount bikes used in each site
siteDict = {}

csvfile = readData('export.csv')
average_computing(csvfile)

export_siteDict()

if siteDict:
    print(len(siteDict.keys()))
    for index in siteDict.keys():
        print(siteDict[index])


