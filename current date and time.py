from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date is:", today)
print("The current date and time are:", now)

print("Date components are:", today.year, today.month, today.day)