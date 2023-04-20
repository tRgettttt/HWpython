# -*- coding: utf-8 -*-
def numbers3(func):
    def wrapper(*args, **kwargs):
        print(f"Данная функция выводит все числа между {args[0]} и {args[1]}")
        return func(*args, **kwargs)
    return wrapper

@numbers3
def Num_del_3(a, b):
    for num in range(a, b+1):
        if num % 3 == 0:
            print(num)

Num_del_3(10, 25)
