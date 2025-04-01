import json

file = open("weather.json","r")
data = file.read()
json_data = json.loads(data)

max_temp = json_data["main"]["temp_max"]
min_temp = json_data["main"]["temp_min"]
sys = json_data["sys"]["sunset"]
print(max_temp)