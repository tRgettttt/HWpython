"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""
def print_values(param1=None, param2=None, param3=None):
    if param1 is not None:
        print("param1:", param1)
    if param2 is not None:
        print("param2:", param2)
    if param3 is not None:
        print("param3:", param3)

print_values(param2 = 30, param3=50)