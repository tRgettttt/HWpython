# -*- coding: utf-8 -*-
def salat(func):
    def wrapper():
        sandwich = func()
        sandwich.append('салат')
        return sandwich
    return wrapper

def pineapple(func):
    def wrapper():
        sandwich = func()
        sandwich.append('ананасы')
        return sandwich
    return wrapper

@salat
@pineapple
def sandwich_recipe():
    ingredients = ["Хлеб", "Колбаса", "Сыр", "Майонез"]
    return ingredients

print(sandwich_recipe())
