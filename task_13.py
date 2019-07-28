l = [54, 31, 333, 65, 12, 7]
index = int(input('Введите номер индекса: '))
try:
	print(l[index])
except IndexError:
	print('Данного индекса нет в списке')