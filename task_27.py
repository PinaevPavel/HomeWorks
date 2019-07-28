def Exception_Handling(func):
	try:
		func()
	except ZeroDivisionError:
		print('Деление на ноль')
	except NameError:
		print('Неверно заданно имя')
	except TypeError:
		print('Ошибка типа')

@Exception_Handling
def addition():
	'a' + 1

@Exception_Handling
def Name_Error():
	a + 1