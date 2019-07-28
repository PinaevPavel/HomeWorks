class Printer(object):
	def __init__(self):
		self.values = []
	def log(self, *values):
		self.values = [v for v in values]
		print(self.values)

pr = Printer()
pr.log(1, 2, 3, 4, 5)

class FormattedPrinter(Printer):
	def formated_log(self, *values):
		print('*****************')
		self.log(*values)
		print('*****************')

pr1 = FormattedPrinter()
pr1.formated_log(5, 4, 3, 2, 1)
