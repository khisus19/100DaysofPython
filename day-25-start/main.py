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


# Create a DataFrame or a table from a dictionary

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)

data.to_csv("new_data.csv")

print(data)