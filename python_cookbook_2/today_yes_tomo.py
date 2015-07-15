#calculate today,yesterday,tomorrow
import datetime
today=datetime.date.today()
yesterday=today.replace(day=today.day-1)
tomorrow=today.replace(day=today.day+1)
print today
print yesterday
print tomorrow
print today.replace(month=today.month+1)

#another method:timedelta
yes=today-datetime.timedelta(days=1)
tom=today+datetime.timedelta(days=1)
print yes
print tom
