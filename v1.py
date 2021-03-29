from datetime import date,timedelta
[dd,mm,yyyy]=list(map(int,input("Birthday format: day-month-year: ").split('-')))
d1 = date(yyyy,mm,dd)
d2 = date.today()
daysold=str((d2 - d1).days)

print("number of days old: ",daysold)
dweekday=d1.weekday()
#print(dweekday)
weekdays=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday']
print("Day of the birth:", weekdays[dweekday])
dya=list(range(1000,51000,1000))

for i in dya:
	year=timedelta(days=i)
	dweekday=(d1+year).weekday()
	print('lived ',i,'days on',d1+year,weekdays[dweekday])
for i in range(10):
	d3 = date(yyyy+i,mm,dd)
	daysold=str((d3 - d1).days)
	print(daysold)