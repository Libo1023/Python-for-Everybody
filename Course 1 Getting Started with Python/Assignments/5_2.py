# Assignment 5.2
# Write a program that repeatedly prompts a user for integer
# numbers until the user enters 'done'. Once 'done' is entered, print
# out the largest and smallest of the numbers. If the user enters
# anything other than a valid number catch it with a try/except and put
# out an appropriate message and ignore the number. Enter 7, 2, bob,
# 10, and 4 and match the output below.

largest = None
smallest = None

while True :
	num_s = input('Enter a number: ')
	
	if num_s == 'done' :
		break

	try :
		num_f = float(num_s)
	except :
		print('Invalid input')
		continue

	if largest is None :
		largest = num_f
	elif num_f > largest :
		largest = num_f
	else :
		largest = largest

	if smallest is None :
		smallest = num_f
	elif num_f < smallest :
		smallest = num_f
	else :
		smallest = smallest

largest_i = int(largest)
smallest_i = int(smallest)
print('Maximum is', largest_i)
print('Minimum is', smallest_i)