# Create a list with the names of friends and colleagues. Calculate the average length of
# the names.

# 2. Create a list with the names of friends and colleagues. Search for the name John using
# a for loop. Print not found if you didn’t find it. (Hint: use else).

# 3. Create a list of tuples of first name, last name, and age for your friends and colleagues.
# If you don’t know the age, put in None. Calculate the average age, skipping over any
# None values. Print out each name, followed by old or young if they are above or below
# the average age.
# from statistics import mean
#
attednace_list = list()
attednace_list.append("Artur")
attednace_list.append("Alicja")
attednace_list.append("Denis")
attednace_list.append("Piotr")
attednace_list.append("Marcin")
attednace_list.append("Laura")
attednace_list.append("Tomasz")
#
# avg_length = mean([ len(name) for name in attednace_list])
# print(avg_length)

for name in attednace_list:
    if 'Tomasz' == name:
        print("Tomasz is present")
        break
else:
    print("Tomasz is not present")

