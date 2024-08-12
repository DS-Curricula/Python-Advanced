import datetime

# Getting the current date and time
now = datetime.datetime.now()
print("Current Date and Time:", now)

# Creating a specific date
specific_date = datetime.date(2023, 8, 5)
print("Specific Date:", specific_date)

# Creating a specific time
specific_time = datetime.time(14, 30, 45)
print("Specific Time:", specific_time)

# Creating a specific datetime
specific_datetime = datetime.datetime(2023, 8, 5, 14, 30, 45)
print("Specific Datetime:", specific_datetime)

# Adding 10 days to the current date
delta = datetime.timedelta(days=10)
future_date = now + delta
print("Future Date:", future_date)
