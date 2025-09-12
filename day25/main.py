import pandas as pd

data = pd.read_csv('weather_data.csv')
print(data)

temp_list = data['temp'].to_list()
print(temp_list)

media_temp = data['temp'].mean()
print(media_temp)

max_temp = data['temp'].max()
print(max_temp)

print(data.condition)
print(data["condition"])

print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
monday_temp = int(monday.temp[0])
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")


