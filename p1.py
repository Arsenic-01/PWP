import calendar

print(calendar.month(2025,4))

import datetime

# Get current date and time
now = datetime.datetime.now()

# Format date and time
current_date = now.strftime("%d/%m/%y")
current_time = now.strftime("%H:%M:%S")

print("Current Date:", current_date)
print("Current Time:", current_time)


from datetime import datetime
now = datetime.now()

print(now)

print(now.day,now.time(),now.date(),now.month,now.year)

