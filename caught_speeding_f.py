## You are driving a little too fast, and a police officer stops you.##
## Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.##
##  If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1.##
##  If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day,##
##  your speed can be 5 higher in all cases.## 

def caught_speeding (speed,is_birthday):
    ticket=None
    if is_birthday == False:
        if speed <=60:
            ticket=0
        elif speed >= 61 and speed <= 80:
            ticket=1          
        elif speed >= 81:
            ticket=2
        print(ticket)

    elif is_birthday == True:
        if speed <=65:
            ticket=0
        elif speed >= 65 and speed <= 85:
            ticket=1
        elif speed >= 86:
            ticket=2
        print(ticket)    

print ('Test 1:0?')
caught_speeding(60, False)

print ('Test 2:1?')
caught_speeding(65, False)

print ('Test 3:0?')
caught_speeding(65, True) 

print ('Test 4:1?')
caught_speeding(80, False) 

print ('Test 5:2?')
caught_speeding(85, False)

print ('Test 6:1?')
caught_speeding(85, True)

print ('Test 6:1?')
caught_speeding(70, False) 

print ('Test 7:1?')
caught_speeding(75, False)

print ('Test 8:1?')
caught_speeding(75, True) 

print ('Test 9:0?')
caught_speeding(40, False) 

print ('Test 10:0?')
caught_speeding(40, True) 

print ('Test 11:2?')
caught_speeding(90, False) 