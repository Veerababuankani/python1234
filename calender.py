#genarating the calender
import calendar
yr=int(input("enter the year:"))
mon=int(input("enter the month:"))
print("#"*100)
print(calendar.TextCalendar().formatyear(yr))
print("#"*100)
print(calendar.month(yr,mon))
print("#"*100)