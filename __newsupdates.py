import requests  # For having multiple requests
import json  # for json file parsing


class NEWS:
    # defined local news method
    def local_news(self):
        try:
            # make a GET request to the API
            try:
                response = requests.get(
                    'http://newsapi.org/v1/articles?source=mirror&sortBy=top&apiKey=2e69f4090e594eb7bab09aedb78338a7')
            except Exception as Ex:
                print("there was an error while contactin the specified API", Ex)  # prints the inner exception
            # load the response from API into JSON
            # print(response.content)
            d = json.loads(response.content.decode())  # Decoding is required to convert from bytes to string
            # print all the articles
            for i in range(0, 4):
                print(d['articles'][i]['title'])
            # write response data to json file
            with open('result.json', 'w') as fp:
                json.dump(d, fp, indent=4)  # Dumps in the file
            return fp  # returns the file to the main thing
        except Exception as Ex:
            print("Unable to return text recieved due to an error recieved at loc(self) function as :",
                  Ex)  # printing the exception

            # defined national news method

    def national_news(self):
        try:
            try:
                response = requests.get(
                    'http://newsapi.org/v1/articles?source=the-new-york-times&sortBy=top&apiKey=2e69f4090e594eb7bab09aedb78338a7')
            except Exception as Ex:
                print("there was an error while contactin the specified API", Ex)  # prints the inner exception
            print(response.content)  # Printing the responce
            e = json.loads(
                response.content.decode())  # use the decode function to pull out the json in the string rather than bytes
            for i in range(0, 4):
                print(e['articles'][i]['title'])  # missing parenthesis in python 3+ verisons

            with open('result.json', 'w') as fp:
                json.dump(e, fp, indent=4)  # indentation ERROR
            return fp  # indentation ERROR
            # defined international news method
        except Exception as Ex:
            print("Unable to return the text due to an error which was recieved at the nat(self) function as :",
                  Ex)  # printing the exception

    def inter(self):
        response = requests.get(
            'http://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=2e69f4090e594eb7bab09aedb78338a7')
        d = json.loads(response.content.decode())  # Loading in the json , as a responce and converting it
        for i in range(0, 4):  # Loopign through each i index
            print(d['articles'][i]['title'])  # use the parenthesis for well formating
        with open('result.json', 'w') as fp:
            json.dump(d, fp, indent=4)
        return fp

    def get_geolocation(self):
        try:
            try:
                freegeoip = "http://freegeoip.net/json"  # A site which provide free geo location address in the json format
            except Exception as Ex:
                print("there was an error while contactin the specified free geo api", Ex)  # prints the inner exception
            geo_r = requests.get(freegeoip)  # requesting the Geo location from the web
            geo_json = geo_r.json()  # Getting the text from the web in the form of json
            print(geo_json["ip"])  # this will prints the specified ip
            user_position = [geo_json["latitude"], geo_json["longitude"]]  # getting the user position
            print("User detected position is at ", geo_json["ip"], "with lag and lat at ", user_position)
        except Exception as Ex:
            print("Unable to find in the location, error in function get_geolocation", Ex)
