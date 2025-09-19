# Simple Birthday Countdown Timer

import datetime
import bday_messages

today = datetime.date.today()  # Get today's date

next_birthday = datetime.date(today.year, 12, 25)  # Set next birthday date (e.g., Christmas)

date1 = today
date2 = next_birthday

time_difference = date2 - date1  # Calculate the difference between the two dates

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"Your birthday is in {time_difference.days} days.")