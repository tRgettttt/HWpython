"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def calculate_mass(height, weight):
    mass = weight / (height ** 2)
    return mass

def process_mass(mass):
    if mass < 18.5:
        print("Недостаточный вес")
    elif mass >= 18.5 and mass <= 25:
        print("ИМТ в норме")
    else:
        print("Избыточный вес")


height = float(input("Введите рост: "))
weight = float(input("Введите вес: "))
mass = calculate_mass(height, weight)
process_mass(mass)