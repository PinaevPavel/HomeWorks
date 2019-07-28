a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
def tu_max(a, b, c):
	l = [a, b, c]
	l.remove(min(l))
	print(l)
tu_max(a, b, c)