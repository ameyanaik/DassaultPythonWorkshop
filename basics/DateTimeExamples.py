from datetime import datetime as dt

# Get the current date and time
currentdt = dt.now()
print(currentdt)

print("Today's day is:", currentdt.day)
print("Microseconds:", currentdt.microsecond)

print(currentdt.ctime())

# POSIX Format - The number of seconds that have passed since 12 AM on 1st Jan 1970
print(currentdt.timestamp())

print(currentdt.timetuple())

#Ordinal Format - For Dates - No of Days that have passed since 1/1/1
print(currentdt.toordinal())

import datetime

#Create a Date Object
mydate = datetime.date(2000,8,25)
print(mydate.toordinal())
print(mydate.weekday())

#strftime('%Y-%m-%d %H:%M:%S'))

print(currentdt.strftime("%A"))
print(currentdt.strftime("%a"))
print(currentdt.strftime("%b"))
print(currentdt.strftime("%d"))
print(currentdt.strftime("%D"))

print(dt.today())

datetime_str = '08/25/21'

datetime_obj = dt.strptime(datetime_str, '%m/%d/%y')

print(datetime_obj)

print(datetime_obj.date())

print(datetime_obj.weekday())

