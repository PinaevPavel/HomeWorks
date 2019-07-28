numer_of_calls = 0

def func5(func):
    if not hasattr(func5, '_state'):  # инициализация значения
        func5._state = 0
    print(func5._state)
    func5._state = func5._state + 1



@func5
def add():
	print(2 * 2 + 2)

@func5
def add():
	print(2 * 2 + 2)

@func5
def add():
	print(2 * 2 + 2)