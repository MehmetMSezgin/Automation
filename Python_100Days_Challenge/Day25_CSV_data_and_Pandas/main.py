"""with open("weather_data.csv") as weather_data:
    data = weather_data.readlines()
    print(data)
"""

'''
import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)
'''

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print("-----------")

print(data["temp"])
print("-----------")

print(type(data))  # Data frame (two dimentional)
print("-----------")

print(type(data["temp"]))  # Series (one dimentional)
print("-----------")

data_to_dict = data.to_dict()
print(data_to_dict)
print("-----------")

temp_list = data["temp"].to_list()
print(sum(temp_list) / len(temp_list))
print(data["temp"].mean())
print("-----------")

data_by_day = data[data.day == "Monday"]
print(data_by_day)
print("#########################")
print("\n")
# Assemble new frame from scratch
my_dict = {"names": ["Ancie", "Bombadil", "Gandalf"],
           "scores": [80, 70, 60]
           }

new_data = pandas.DataFrame(my_dict)
new_data.to_csv("Wizards.csv")
