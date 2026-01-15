def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

print(spam(0))
print(spam(1))
print(spam(2))
print(spam(12))
