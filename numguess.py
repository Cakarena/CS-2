##Program Name: numguess.py 
##Write a Python program to guess a number between 1 to 9. 
##Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, 
## on successful guess, user will get a "Well guessed!" message, and the program will exit. Hint: Use the random function. 


import random
target_number, guess_number=random.randint(0,3),0
while target_number != guess_number:
	guess_number = int(input('Guess a number between 1 and 10 until you get it right : '))
	if (guess_number > target_number or guess_number < target_number):
		print("try again...you were soooo close")
	else:
		print("Well Guessed")
		exit()
