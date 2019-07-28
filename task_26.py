def benchamark(func):
	print('Создан декоратор')
	print('Начало выполения функции')
	func()
	print('Закончено выполнение функции')
	return 

@benchamark
def add():
	print(2 * 2 + 2)

