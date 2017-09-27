def sleep_in (Weekday, Vacation):
	sleep=None
	if not Weekday == False and Vacation == False:
		sleep=False
	else:
		sleep=True
	print(sleep)

print ('Test Case 1')
sleep_in(False, False)

print ('Test Case 2')
sleep_in(True, False)

print ('Test Case 3')
sleep_in(False, True)

print ('Test Case 4')
sleep_in(True, True)
