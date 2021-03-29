from datetime import date,timedelta
datetrue=True
while datetrue:
	try:
		name=input("what is your name:").replace(" ", "_") + '.txt'
		[dd,mm,yyyy]=list(map(int,input("Birthday format: day-month-year: ").split('-')))
		d1 = date(yyyy,mm,dd)
		d2 = date.today()
		daysold=str((d2 - d1).days)
		dweekday=d1.weekday()
		weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

		dya=list(range(1000,51000,1000))
		with open(name,'a+') as f:
			f.write('Welcome to Milestones in Life! \nThanks '+name[:-4].replace('_',' ') +' for choosing us!\nWishing you many more Happy moments return on your Milestones.\n')
			f.write("Number of days old: "+str(daysold)+'\n')
			f.write("Day of the birth: "+ str(weekdays[dweekday])+'\n')
			for i in dya:
				year=timedelta(days=i)
				dweekday=(d1+year).weekday()
				f.write("Milestone of " + str(i)+ ' days on '+str(d1+year)+' on '+str(weekdays[dweekday])+'\n')
				#print('lived ',i,'days on',d1+year,weekdays[dweekday])
			print("Thanks for using Milestones in Life")
		datetrue=False
	except ValueError:
		print('Date is invalid.. Try again')
		#[dd,mm,yyyy]=list(map(int,input("Birthday format: day-month-year: ").split('-')))
