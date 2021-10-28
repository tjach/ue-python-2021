# Create a variable that points to a floating point number. Examine the id, type, and
# value of that number. Update the variable by adding 20 to it. Re-examine the id, type,
# and value. Did the id change? Did the value change?


# 2. Create a variable pointing to an empty list. Examine the id, type, and value of the list.
# Append the number 300 to the list. Re-examine the id, type, and value. Did the id
# change? Did the value change?

from typing import Union, List


def identity(input_value: Union[float, List]):
    print(f"Value: {input_value}, id: {id(input_value)}, type: {type(input_value)}")


floating_point = 4.2
identity(floating_point)
floating_point = 4.3
identity(floating_point)


empty_list = []
identity(empty_list)

