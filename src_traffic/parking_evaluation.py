import pandas as pd
import csv


def parksituation(time = ("12:30")):

    xls = pd.ExcelFile("../data/9_Car_Parking_Data.xls")
    sheetX = xls.parse(0) #2 is the sheet number
    alle_werte = sheetX.values
    time_interval = sheetX["Parkhaus"]

    i = 2
    for x in time_interval:
        if str(x) == time:

            P00_p = int(alle_werte[i][1]) / int(alle_werte[0][1])
            #alternativ int(P02[i]) / int(P02[0])

            P02_p = int(alle_werte[i][2]) / int(alle_werte[0][2])

            P03_p = int(alle_werte[i][3]) / int(alle_werte[0][3])

            P04_p = int(alle_werte[i][4]) / int(alle_werte[0][4])

            P05_p = int(alle_werte[i][5]) / int(alle_werte[0][5])

            P06_p = int(alle_werte[i][6]) / int(alle_werte[0][6])

            P07_p = int(alle_werte[i][7]) / int(alle_werte[0][7])

            P08_p = int(alle_werte[i][8]) / int(alle_werte[0][8])

            P09_p = int(alle_werte[i][9]) / int(alle_werte[0][9])

            P11_p = int(alle_werte[i][10]) / int(alle_werte[0][10])

            P2021_p = (int(alle_werte[i][11]) + int(alle_werte[i][12])) / int(alle_werte[0][11])

            P2223_p = (int(alle_werte[i][13]) + int(alle_werte[i][14])) / int(alle_werte[0][13])

            P25_p = int(alle_werte[i][15]) / int(alle_werte[0][15])

            P26_p = int(alle_werte[i][16]) / int(alle_werte[0][16])

            parkhaus_p = [P00_p, P02_p, P03_p, P03_p, P04_p, P04_p, P05_p, P06_p, P07_p, P08_p, P09_p, P11_p, P2021_p, P2223_p, P25_p, P26_p]
            return parkhaus_p
        i += 1

def all_parksituation():

    xls = pd.ExcelFile("../data/9_Car_Parking_Data.xls")
    sheetX = xls.parse(0) #2 is the sheet number
    alle_werte = sheetX.values
    time_interval = sheetX["Parkhaus"]
    i = 2
    with open('../data/Car_Parking_Data.csv', mode='w') as csv_file:
        parking_data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        parking_data.writerow(["Timestamp","P00", "P02", "P03", "P03", "P04", "P04", "P05", "P06", "P07", "P08", "P09", "P11", "P2021", "P2223", "P25", "P26"])
        for x in time_interval[2:]:
            P00_p = int(alle_werte[i][1]) / int(alle_werte[0][1])
            #alternativ int(P02[i]) / int(P02[0])

            P02_p = int(alle_werte[i][2]) / int(alle_werte[0][2])

            P03_p = int(alle_werte[i][3]) / int(alle_werte[0][3])

            P04_p = int(alle_werte[i][4]) / int(alle_werte[0][4])

            P05_p = int(alle_werte[i][5]) / int(alle_werte[0][5])

            P06_p = int(alle_werte[i][6]) / int(alle_werte[0][6])

            P07_p = int(alle_werte[i][7]) / int(alle_werte[0][7])

            P08_p = int(alle_werte[i][8]) / int(alle_werte[0][8])

            P09_p = int(alle_werte[i][9]) / int(alle_werte[0][9])

            P11_p = int(alle_werte[i][10]) / int(alle_werte[0][10])

            P2021_p = (int(alle_werte[i][11]) + int(alle_werte[i][12])) / int(alle_werte[0][11])

            P2223_p = (int(alle_werte[i][13]) + int(alle_werte[i][14])) / int(alle_werte[0][13])

            P25_p = int(alle_werte[i][15]) / int(alle_werte[0][15])

            P26_p = int(alle_werte[i][16]) / int(alle_werte[0][16])

            print([x, P00_p, P02_p, P03_p, P03_p, P04_p, P04_p, P05_p, P06_p, P07_p, P08_p, P09_p, P11_p, P2021_p, P2223_p, P25_p, P26_p])
            parking_data.writerow([x, P00_p, P02_p, P03_p, P03_p, P04_p, P04_p, P05_p, P06_p, P07_p, P08_p, P09_p, P11_p, P2021_p, P2223_p, P25_p, P26_p])
            i += 1
            if i > 97:
                break



if __name__ == "__main__":
    all_parksituation()



