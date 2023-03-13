first = "0 0 0 0 0 0 0" #Вывод должен быть 0
second = "1 1 1 0 0 0 0" # Вывод должен быть 3
third = "1 1 1 1 1 1 1" # Вывод должен быть 1

tasks = [int(x) for x in third.split()]
count = 0

abc = [i for i in tasks[:3] if i != 0]
links = tasks[3:].count(1)

for i in range(links):
    if len(abc) >= 2:
        abc.append(list({abc.pop(0), abc.pop(0)})[0])

print(len(abc))