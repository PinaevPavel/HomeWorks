number = int(input('Insert the number '))
try:
	if number > 10:
		raise ValueError
	elif number < 0:
		raise TypeError
	elif number % 2 == 0:
		raise IndexError
except ValueError:
	print('You entered an even number. Error')
except TypeError:
	print('You have entered a number less than 0. Error')
except IndexError:
	print('You have entered a number more than 10. Error')
else:
	print('You have entered the correct number')