import requests

class DataManager():

    def get_amsID(self, flight_number , from_time , till_time):

        URL = "http://fsg-datahub.azure-api.net/legacy/Apps/AirportSTR/Flights/Get"
        HEADERS = {"Ocp-Apim-Subscription-Key":"e9dddf3b02c04ac98d341b24036bc18f"}
        PARAMS = {"from":from_time,"till":till_time,"Name":flight_number}

        data = requests.get(url=URL,headers=HEADERS,params=PARAMS)

        flight_list = data.json()

        for f in flight_list:
                if f["Name"] == flight_number:
                        flight_information = f

        print(flight_information)


if __name__ == "__main__":
    data_manager = DataManager()

    data_manager.get_amsID("EW 2964","2019-10-26T01:09:21","2019-10-26T21:09:21")
