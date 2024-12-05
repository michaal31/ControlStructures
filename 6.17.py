
time_24 = input("Enter time (24-hour format): ")
    
hour, minute = map(int, time_24.split(":"))
if hour == 0:
        hour_12 = 12
        period = "am"
elif hour < 12:
        hour_12 = hour
        period = "am"
elif hour == 12:
        hour_12 = 12
        period = "pm"
else:
        hour_12 = hour - 12
        period = "pm"
minute_str = f"{minute:02d}"
print(f"Time in 12-hour format: {hour_12}:{minute_str}{period}")



