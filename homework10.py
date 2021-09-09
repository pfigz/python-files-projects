#Homework 10: Importing -> Calendar

#Import the module
import calendar as c

# calendar.setfirstweekday(weekday) sets the starting day for each week. Default is Monday (EU standard)

#Set starting weekday to SUNDAY (US Standard)
c.setfirstweekday(c.SUNDAY)

# calendar.calendar returns a calendar for an entire year with parameters: calendar(year, w, l, c, m)
# w = date column width
# l = line spaces between weeks
# c = spaces between month columns
# m = number of month columns

# Set parameters for calendar year 2020
year_2020 = c.calendar(2020, 2, 1, 4, 3)
print(year_2020)

# calendar.isleap(year) -> returns True if (year) is a leap year
leap_year = c.isleap(2020)
print(leap_year)

# calendar.leapdays(y1, y1) returns number of leap years in range (y1, y2)
leap_days = c.leapdays(2000, 2020)
print("There were " + str(leap_days) + " leap years in the range selected.")

# calendar.weekday(y, m, d) -> returns day of the week where 0 = Monday, 1 = Tuesday, etc.:
# y = year
# m = month(1-12)
# d= date(1-31)

# Return day of the week (0-6) for December 31, 2020:
day_of_week = c.weekday(2020, 12, 9)
weekday = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

for key in weekday:
    if key == day_of_week:
        print("The day of the week for the selected date is " + weekday[key] + ".")




