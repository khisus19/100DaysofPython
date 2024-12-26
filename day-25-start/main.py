# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv('./weather_data.csv')


# # Convert a DataFrame to a Dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # Convert a row to a list
# temp_list = data["temp"].to_list()

# final_sum = sum(temp_list)
# average_temp = final_sum / len(temp_list)

# average_temp = data["temp"].mean()
# maximum_temp = data["temp"].max()

# print(maximum_temp)
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_far_temp = (monday.temp[0] * 9/5) + 32
# print(monday_far_temp)


# # Create a DataFrame or a table from a dictionary

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# print(data)

data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrel_list = data[data["Primary Fur Color"] == "Gray"]
red_squirrel_list = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel_list = data[data["Primary Fur Color"] == "Black"]

squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(grey_squirrel_list), len(red_squirrel_list), len(black_squirrel_list)]
}

squirrel_table = pd.DataFrame(squirrel_dict)
squirrel_table.to_csv("squirrel_count.csv")