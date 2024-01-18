"""
DATETIME:
-Time values are represented with the time class and have attributes for hour, minute, second,
and microsecond.
-Date values are created using Date() class and have attributes for year, month, and day.
"""

import datetime
import time


# -----------------DATETIME-----------------

t = datetime.time(4, 20, 1)
today = datetime.date.today()

# Display the different time components
print(t)
print('hour:', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)

# Display the different date components
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)

# Calculate differences in dates
# Using datetime.timedelta to calculate past or future days
# Pass weeks, days, hours, minutes, seconds, milliseconds, microseconds as argument to timedelta
now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days=1)
next_week = now + datetime.timedelta(weeks=1)
one_hour_less = now - datetime.timedelta(hours=1)




# -----------------TIME-----------------

# sleep() -> suspend (delay) execution of the current thread for the given number of seconds
time.sleep(2)

# time() -> return the number of seconds passed since epoch
# For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where time begins)
# Useful function to get files from a past date to now
now = time.time()
past_7days = now - 86400*7

# ctime(n) -> take seconds passed since epoch and return a string representing local time
local_time = time.ctime(now)
print("Local time: ", local_time)

# strftime(format) -> print current time as a string in the given format
# Most used characters for time format
# %a - abbreviated weekday name
# %A - full weekday name
# %b - abbreviated month name
# %B - full month name
# %d - day of the month (01 to 31)
# %D - same as %m/%d/%y
# %e - day of the month (1 to 31)
# %H - hour, using a 24-hour clock (00 to 23)
# %I - hour, using a 12-hour clock (01 to 12)
# %m - month (01 to 12)
# %M - minute
# %n - newline character
# %p - either am or pm according to the given time value
# %r - time in a.m. and p.m. notation
# %R - time in 24 hour notation
# %S - second
# %t - tab character
# %T - current time, equal to %H:%M:%S
# %x - preferred date representation without the time
# %X - preferred time representation without the date
# %y - year without century
# %Y - year with century as a decimal number
# %% - a literal % character
print(time.strftime("%b %d %Y %H:%M:%S"))
print(time.strftime('%Y-%m-%d:%H:%M:%S'))
