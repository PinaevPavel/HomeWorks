class Person(object):
	kith = []
	def __init__(self, age, name):
		self.age = age
		self.name = name
	def know(self, name):
		return self.kith.append(name)
	def is_known(self, name):
		if name in self.kith:
			print('familiar with', name)
		else:
			print('not familiar', name)

Pavel = Person(25, 'Pavel')
Pavel.know('Vasa')
Pavel.know('Bender')
Pavel.is_known('Bender')
Pavel.is_known('Zayka')
print(Pavel.age)
print(Pavel.name)
print(Pavel.kith)