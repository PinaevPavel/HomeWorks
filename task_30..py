def decorator(func):
	func.counter = 1
	def fake(value):
		print('Runs:', func.counter)
		func.counter += 1
		return func(value)
	return fake

@decorator
def my_str(value):
	return str(value)


print(my_str(123))
print(my_str([]))
print(my_str({}))