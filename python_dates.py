#python dates
from datetime import date, timedelta

today = date.today()
print(today.day)
print(today.weekday())
f_date = today.strftime("%d/%m/%Y")
print(f_date)

expiry_date = today + timedelta(days=30)
print(expiry_date)

date1=date(2006,3, 16)
date2=date(1997 ,5 ,26)
diff=date1-date2
print(diff.days)
