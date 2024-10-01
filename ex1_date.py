# from datetime import datetime 
# from datetime import timedelta
from datetime import datetime, timedelta

#1 Getting the Current Date and Time:

now = datetime.now()  # current date and time
print(now)

#2 Formatting Dates and Times:
fmt_now = now.strftime("%Y-%m-%d %H:%M:%S")
print(fmt_now)

#3 Parsing Dates from Strings:
date_str = "2024-09-02"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
print(date_obj)

#4 Date Arithmetic: Add or subtract dates using timedelta:
tomorrow = now + timedelta(days=1)
print(tomorrow)




# Get current time
now = datetime.now()

# Calculate the date 10 days from now
future_date = now + timedelta(days=10)

# Format the future date as a string
future_date_str = future_date.strftime("%Y-%m-%d %H:%M:%S")
print(future_date_str)