import sys

def get_numbers():
	start = 0
	end = 10
	step = 1
	while start < end:
		yield start
		start += step

gen = get_numbers()

print(next(gen))
print(next(gen))
print(list(gen))
try:
	gen = get_numbers()
	for i in gen:
		print(i)
except StopIteration as e:
	print(e)