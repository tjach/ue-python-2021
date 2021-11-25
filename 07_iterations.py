# Create a list with the names of friends and colleagues. Calculate the average length of
# the names.

# 2. Create a list with the names of friends and colleagues. Search for the name John using
# a for loop. Print not found if you didn’t find it. (Hint: use else).

# 3. Create a list of tuples of first name, last name, and age for your friends and colleagues.
# If you don’t know the age, put in None. Calculate the average age, skipping over any
# None values. Print out each name, followed by old or young if they are above or below
# the average age.

# 4. Write a simple program which tells if a number is prime

def is_prime(number: int):
    for divider in range(2,number):
        if not number % divider:
            print(f"Not prime! Divisable by {divider}")
            break
    else:
        print("Number is prime!")

is_prime(5)