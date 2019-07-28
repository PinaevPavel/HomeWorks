def case_tu(l = ['a', 'B', 'c'], case = None):
	if case == True:
		l = [x.upper() for x in l]
		print(l)
	elif case != True:
		l = [x.lower() for x in l]
		print(l)
case_tu()