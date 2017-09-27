## Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat,##
##  and a boolean indicating if we are on vacation, return a string of the form "7:00"##
##  indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00"##
##  and on the weekend it should be "10:00". Unless we are on vacation ##
## -- then on weekdays it should be "10:00" and weekends it should be "off".## 

def alarm_clock(vacation, day):
	alarm=None
	if vacation==False and (day >=1 and day <=5):
		alarm=7.00
	elif vacation==False and (day == 0 or day == 6):
		alarm=10.00
	elif vacation==True and (day == 0 or day ==6):
		alarm='off'
	elif vacation==True and (day >=1 and day <=5):
		alarm=10.00
	print(alarm)

alarm_clock(False,1)
alarm_clock(False,5)
alarm_clock(False,0)
alarm_clock(False,6)
alarm_clock(True,0)
alarm_clock(True,6)
alarm_clock(True,1)
alarm_clock(True,3)
alarm_clock(True,5)

