def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(0))
    print(spam(1))
    print(spam(2))
    print(spam(12))
except ZeroDivisionError:
    print("Can't divide by zero!")


