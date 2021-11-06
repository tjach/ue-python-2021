# Create a variable that points to a floating point number. Examine the id, type, and
# value of that number. Update the variable by adding 20 to it. Re-examine the id, type,
# and value. Did the id change? Did the value change?

# var_float = 42.0
# print(id(var_float))
# var_float = "ala ma kota"
# print(id(var_float))

# zmienna: str = 42.0
#
# print(zmienna)


# 2. Create a variable pointing to an empty list. Examine the id, type, and value of the list.
# Append the number 300 to the list. Re-examine the id, type, and value. Did the id
# change? Did the value change?

def print_object_info(what: list):
    print(what)
    print(id(what))
    print(type(what))
    return True


lista = list()
print_object_info(lista)

lista.append(300)
print_object_info(lista)


