import requests
import datetime

class DataManager():

    # basic flight information as root point for data extraction
    flight_information = None

    # id of the flight
    amsID = None

    def get_departure(self):

        URL = "http://fsg-datahub.azure-api.net/legacy/Apps/AirportSTR/Flights/GetDeparture/"+str(self.amsID)
        HEADERS = {"Ocp-Apim-Subscription-Key":"e9dddf3b02c04ac98d341b24036bc18f"}
        #PARAMS = {"amsid":self.amsID}

        data = requests.get(url=URL,headers=HEADERS)
        departure_data = data.json()

        departure = datetime.datetime.strptime(departure_data["Plan"],"%Y-%m-%dT%H:%M:%S")

        return departure

        #datetime.datetime.strptime(time_of_flight, '%d-%m-%Y').date()


    def set_flight(self, flight_number, time_of_flight):

        from_time = datetime.datetime.strptime(time_of_flight, '%d/%m/%Y').date()
        till_time = from_time + datetime.timedelta(days=1)

        URL = "http://fsg-datahub.azure-api.net/legacy/Apps/AirportSTR/Flights/Get"
        HEADERS = {"Ocp-Apim-Subscription-Key":"e9dddf3b02c04ac98d341b24036bc18f"}
        PARAMS = {"from": from_time,"till":till_time,"Name":flight_number}

        data = requests.get(url=URL,headers=HEADERS,params=PARAMS)

        flight_list = data.json()

        for f in flight_list:
                if f["Name"] == flight_number:
                        self.flight_information = f

        self.amsID = self.flight_information["AmsId"]

    def get_flight_information(self):
        return self.flight_information

if __name__ == "__main__":
    data_manager = DataManager()

    data_manager.set_flight("EW 2964","26/10/2019")
    print(data_manager.get_flight_information())
    print(data_manager.get_end_time())
