class Animal(object):
	def __init__(self, name, denger):
		self.name = name
		self.dangerous = self.is_dangerous(denger)
	def is_dangerous(self, denger):
		if denger == 'хишник' or denger == 'ядовитый':
			return True
		else:
			return False

Kat = Animal('Barsik', 'Котик')
print(Kat.dangerous)
Wolf = Animal('Gray', 'хишник')

class Human(object):
	def __init__(self, name):
		self.name = name
	def danger_check(self, unit):
		if unit.dangerous == True:
			print('Данное существо опасно для человека')
		else:
			print('Данное существо не опасно для человека')

vasya = Human('Vasya')
vasya.danger_check(Kat)
vasya.danger_check(Wolf)