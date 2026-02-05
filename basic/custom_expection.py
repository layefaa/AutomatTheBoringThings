class AgeError(Exception):
    "Raised when the age is invalid"
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeError("Age must be non-negative")
except AgeError as e:
    print(e)
else:
    print("You are old enough to vote!")
finally:
    print("Goodbye!")

