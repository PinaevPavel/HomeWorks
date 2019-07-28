x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
def inp(x, y):
	if (x > 0) and (y > 0):
		print(x + y)
	elif (x < 0) and (y < 0):
		print(x - y)
	elif (x > 0 and y < 0) or (x < 0 and y > 0):
		print(0)
inp(x, y)