weather_c = {
    "Monday": 12,
    "Tuesday": 23,
    "Wednesday": 34,
    "Thursday": 45,
    "Friday": 31,
    "Saturday": 24,
    "Sunday": 12,
}

def get_f_from_c(temp_c):
    return (temp_c * 9/5) + 32


weather_f = {day:get_f_from_c(temp) for (day, temp) in weather_c.items()}

print(weather_f)
