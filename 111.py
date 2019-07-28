def fib():
    """
    :return: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

x = fib()
print(next(x))
print(next(x))  # OOPS
print(next(x))