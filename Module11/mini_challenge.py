import datetime

# 1. Get the current date and time
current_datetime = datetime.datetime.now()

# Print the individual components
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)
print("Microsecond:", current_datetime.microsecond)

# 2. Calculate the date 100 days in the future
future_date = current_datetime + datetime.timedelta(days=100)
print("Date 100 days in the future:", future_date)

# Calculate the date 100 days in the past
past_date = current_datetime - datetime.timedelta(days=100)
print("Date 100 days in the past:", past_date)

# 3. Create a datetime object for September 1, 2024, at 08:00:00
specific_datetime = datetime.datetime(2024, 9, 1, 8, 00, 0)

# Write the specific datetime to a file
with open('formatted_dates.txt', 'w') as file:
    file.write("Specific datetime: " + specific_datetime.strftime('%Y-%m-%d %H:%M:%S') + '\n')

print("Specific datetime written to 'formatted_dates.txt'.")
