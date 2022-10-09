import pandas as pd

# # Converting a csv to a pandas DataFrame
# data = pd.read_csv("weather_data.csv")
# print(data)

# # Printing a pandas Series
# temps = data.temp
# print(temps)

# # Using built-in class functions
# max_temp = data.temp.max()
# print(max_temp)

# # Printing a row and a specific data from a DataFrame
# monday = data[data.day == "Monday"]
# print(monday)
# print(monday.condition)

# # Converting a Series into a list
# temp_list = data.temp.to_list()
# print(temp_list)

# # Converting a DataFrame into a dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # Creating a DataFrame from scratch
# my_dict = {
#     "a": [1, 2, 3],
#     "b": [4, 5, 6],
# }
# my_data = pd.DataFrame(my_dict)
# print(my_data)

# # Converting a DataFrame into a csv file and saving it
# my_data.to_csv("my_data.csv")


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Getting the number of each primary fur colour and creating a csv file with the data
fur_colour = data["Primary Fur Color"]
fur_colour_df = fur_colour.value_counts()
fur_colour_df.to_csv("squirrel_count.csv")