import requests

api_file = open("apikey.txt", "r")
api_key = api_file.read()
api_file.close()

home = "chicago"

work = "new york"

url = "http://maps.googleapis.com/map/api/distancematrix/json?units=imperial&"

r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key)

time = r.json()["rows"][0]["elements"][0]["duration"]["text"]


print("\nTổng thời gian nhanh nhất để đi từ nhà đến nơi làm việc của bạn là", time)
