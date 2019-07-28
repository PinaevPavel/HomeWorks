def error(value=None):
	x = None
	import random
	if value == None:
		x = random.randint(1, 3)
	try:
		if x == 1:
			raise ValueError
		elif x == 2:
			raise TypeError
		elif x == 3:
			raise RuntimeError
		else:
			1 /int(value)
	except ValueError:
		print('123')
	except TypeError:
		print('321')
	except RuntimeError:
		print('Recurs')
error()