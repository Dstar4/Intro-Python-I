"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""
import sys
import calendar
from datetime import datetime
from sys import argv

cal = calendar
d = datetime.now()

if len(argv) == 1:
    print(d.month)

elif len(argv) == 2:
    month = int(argv[1])
    currentYear = d.year
    print(cal.monthcalendar(currentYear, month))

elif len(argv) == 3:
    month = int(argv[1])
    year = int(argv[2])
    print(cal.monthcalendar(year, month))

else:
    print("The format expected does not match the input")
