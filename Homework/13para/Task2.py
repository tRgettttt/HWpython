"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open("filea2.txt", "w+") as f:
    f.write(' но у меня не получается')

with open("filea.txt", "r") as f1, open("filea2.txt", "r") as f2, open("final.txt", "w+") as f3:
    f3.write(f1.read())
    f3.write(f2.read())