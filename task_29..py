import random
def rand():
	a = random.randint(1, 10000000)
	while True:
		yield a
		a = random.randint(1, 10000000)

x = rand()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
