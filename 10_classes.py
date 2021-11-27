# Scopes and Namespaces Example
# A first class
# Constructors, self, init, class vs object variables
# Methods, private/protected/public
# Inheritance, super
# Operator Overloading def __str__(self):
# @property


























# def scope_test():
#     def do_local():
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
# scope_test()
# print("In global scope:", spam)



# # Using @property decorator
# class Celsius:
#     def __init__(self, temperature=0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#
#     @property
#     def temperature(self):
#         print("Getting value...")
#         return self._temperature
#
#     @temperature.setter
#     def temperature(self, value):
#         print("Setting value...")
#         if value < -273.15:
#             raise ValueError("Temperature below -273 is not possible")
#         self._temperature = value
#
#
# # create an object
# human = Celsius(37)
#
# print(human.temperature)
#
# print(human.to_fahrenheit())
#
# coldest_thing = Celsius(-300)