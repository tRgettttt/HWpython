"""
Напишите список функций по требованию. Пользователь вводит имя.
Если имя заканчивается на А,Я,Г,М, то программа добавляет к имени "Гений".
Если на О,Ь,Л,Н. То добавляется "Сверхразум". Если ни на одну из этих букв то добавляется "Просто" перед именем.
"""
name = input("Введите имя: ")
prosto = lambda name: f"Просто {name}" if name[-1] not in "АЯГМОЬЛН".lower() else name
genius = lambda name: f"{name} Гений" if name[-1] in "АЯГМ".lower() else name
sverh = lambda name: f"{name} Сверхразум" if name[-1] in "ОЬЛН".lower() else name

name = prosto(name)
name = genius(name)
name = sverh(name)

print(name)
