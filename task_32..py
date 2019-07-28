s = [1, 2, 3]
v = ['a', 'b', 'c']

def myreduce(func, array, initial = 0):
	for item in array:
		result = func(item)

z = myzip(s, v)
print(next(z)) 
print(next(z))