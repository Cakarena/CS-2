## We have a loud talking parrot. The "hour" input is the current hour time in the range 0..23.##
## We are in trouble if the parrot is talking and the hour is before 7 or after 20.## 
## Return True if we are in trouble.##

def parrot_trouble(parrot_talk, hour):
	trouble=None
	if parrot_talk == True and (hour < 7 or hour > 20):
		trouble=True
	elif parrot_talk == True and (hour > 7 or hour < 20):
		trouble=False
	else:
		trouble=False
	print(trouble)

parrot_trouble(True,6)
parrot_trouble(True,7)
parrot_trouble(False,6)
parrot_trouble(True,21)
parrot_trouble(False,21)
parrot_trouble(False,20)
parrot_trouble(True,23)
parrot_trouble(False,23)
parrot_trouble(True,20)
parrot_trouble(False,12)