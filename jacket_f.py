##Write a program to accept the temperature value and to tell a person to bring heavy jacket 
##if temperature is < 20, if temperature is between 20 and 30, bring light jacket. 
##if temperature > 30, do not bring any jacket.

def bring_jacket(temp, headingout):
	if headingout == True:
		if temp < 20:
			jacket=2
			print('heavy jacket')
		elif temp <= 30 and temp >= 20:
			jacket=1
			print('light jacket')
		elif temp > 30:
			jacket=0
			print('no jacket')
	elif headingout == False:
		print('no jacket')	

bring_jacket(20,True)
bring_jacket(31,True)
bring_jacket(58,True)
bring_jacket(5,True)
bring_jacket(25,True)
bring_jacket(31,False)

