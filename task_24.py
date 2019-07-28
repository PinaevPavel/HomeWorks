def benchamark(func):
	import time

	def wrapper():
		start = time.time()
		func()
		end = time.time()
		print('[*] Время выполнения: {} секуд.'.format(end - start))
	return wrapper

@benchamark
def add():
	print(2 * 2 + 2)

add()