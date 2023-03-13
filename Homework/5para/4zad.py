academic_staff = []
used_last_names = []
last_name = ''

while True:
    list_of_pupils = []
    last_name = str(input("Введите имя: "))

    if last_name == ' ':
        break
    elif last_name in used_last_names:
        print("этот учитель уже есть в списке.")
        continue
    else:
        used_last_names.append(last_name)

    position = str(input("введите должность: "))
    number_of_pupils = int(input("кол-во студентов: "))

    while number_of_pupils != 0:
        list_of_pupils.append(number_of_pupils)
        number_of_pupils = int(input("кол-во стуентов: "))

    academic_staff.append([last_name, position, list_of_pupils])

print(academic_staff)