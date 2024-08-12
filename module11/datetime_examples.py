import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)
print("Microsecond:", current_datetime.microsecond)

# Get the current date
current_date = datetime.datetime.now().date()

print("Year:", current_date.year)
print("Month:", current_date.month)
print("Day:", current_date.day)

# Get the current time
current_time = datetime.datetime.now().time()

# Define a specific time
time_object = datetime.time(12, 30, 45, 123456)

print("Hour:", time_object.hour)
print("Minute:", time_object.minute)
print("Second:", time_object.second)
print("Microsecond:", time_object.microsecond)


# Get a specific date
specific_date = datetime.date(2024, 4, 5)

# Get a specific time
specific_time = datetime.time(12, 30, 0)

# Create a timedelta representing a duration of time
duration = datetime.timedelta(days=5, hours=3)

# Adding a timedelta to a date
new_date = current_date + duration
print(new_date)

# Subtracting a timedelta from a date
previous_date = current_date - duration
print(previous_date)

# Get the current UTC time
utc_time = datetime.datetime.now(datetime.timezone.utc)
print("Current UTC time:", utc_time)

# Define a custom time zone offset of UTC+3 hours
custom_offset = datetime.timedelta(hours=3)

# Get the current time in the custom time zone
custom_time = utc_time.replace(tzinfo=datetime.timezone(custom_offset))
print("Current time in custom time zone (UTC+3):", custom_time)
