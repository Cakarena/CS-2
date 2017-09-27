##We have two monkeys, a and b. Accept the input telling if each is smiling. 
##We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
##Make sure all test cases below will pass. 
##monkey_trouble(monkey a is smiling, monkey b is smiling)
## (True, True)= True, (False, False) = True, (True, False) = False, (False,True) = False


def monkey_trouble(a_smile, b_smile):
    response=None
    if not a_smile == b_smile: 
    	response=False
    else: 
    	response=True
    print(response)

print ('Test Case 1')
monkey_trouble(True, True)

print ('Test Case 2')
monkey_trouble(False, False)

print ('Test Case 3')
monkey_trouble(True, False)

print ('Test Case 4')
monkey_trouble(False, True)