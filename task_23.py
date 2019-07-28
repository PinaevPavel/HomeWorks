def return_func(func):
	return(print(func.__name__,"is canceled!"))

def pr():
	print('Hello')

@return_func
def pr_1():
	print('Word')

pr()
