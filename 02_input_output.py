# 1. Create some Python code that will prompt you to enter your name. Print out Hello and then the name.
# 2. Create a program that will ask a user how old they are. Print out some text telling them how old they will be next year.

# ad 1
name = input()
print(f"Hello {name.lower()}")


# ad 2
try:
    age = input()
    print(int(age) + 1)
except ValueError as e:
    pass