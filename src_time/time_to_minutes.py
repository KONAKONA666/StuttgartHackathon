import pandas as pd
import csv


def time_to_minutes_Parking(terminal = "T1", timestamp="12:30"):
    path_to_parking_data = '../data/Car_Parking_Data.csv'
    path_to_walking_time = '../data/walking_time_parking deck.csv'

    parking_data = pd.read_csv(path_to_parking_data)
    walking_time = pd.read_csv(path_to_walking_time)

    i = 0
    for x in parking_data["Timestamp"]:
        if x == timestamp:
            parkspace_p = parking_data[i:i+1]
        i += 1

    i = 0
    for x in walking_time["Terminal"]:
        if x == terminal:
            walking_time_form_parkspace_terminal = walking_time[i:i + 1]
        i += 1
    time_array = []
    for x in walking_time_form_parkspace_terminal.iloc[0]:
        try:
            if int(x) < 100:
                time_array.append(x)
        except:
            pass

    i = 0
    j = 0
    for x in parkspace_p.iloc[0]:
        if i in [1,4,5,6,7]:
            time_array[j] += time_array[j]*x
            j += 1
        i += 1

    #Timearray is Array in Minutes for the time to go from Parkingspace [P00,P04,P05,P06,P07] to the Terminal
    return time_array




if __name__ == "__main__":
    time_array = time_to_minutes_Parking(terminal= "T1", timestamp= "12:30")
    i = 0
    for x in ["POO","P04","P05","P06","P07"]:
        print("Time from", x ,"to Terminal 1: ",time_array[i])
        i += 1




