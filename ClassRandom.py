import random 

class Riddler(object):
	

	def __init__(self, number, s):
		self.number = number
		random.seed(s)

	#

	def new_number(self):
		
		self.number = random.randint(1, 100)
		print('Загадано число',self.number)






x = Riddler(None, 3)

x.new_number()
print(x.number)
x.new_number()

print(x.number)
x.new_number()

print(x.number)
x.new_number()

print(x.number)
x.new_number()

print(x.number)
