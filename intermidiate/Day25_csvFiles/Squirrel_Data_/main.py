# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
#



# import csv
# temperatures = []
# with open("weather_data.csv") as data_file:
#     data= csv.reader(data_file)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         else:
#             continue
#
# print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(sum(temp_list)/ len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data["temp"].max()])

# data_dict = {
#     "students": ["Amy", "Sam", "Shmopshik"],
#     "scores": [ 0,1,100]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")





import pandas
data = pandas.read_csv("Squirrel_Data.csv")
gray_count = (len(data[data["Primary Fur Color"] =="Gray"]))
black_count = (len(data[data["Primary Fur Color"] =="Black"]))
cinnamon_count = (len(data[data["Primary Fur Color"] =="Cinnamon"]))
print(gray_count)
print(black_count)
print(cinnamon_count)
data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count":[gray_count,black_count,cinnamon_count ]
}
print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Color_Amount_Data.csv")
