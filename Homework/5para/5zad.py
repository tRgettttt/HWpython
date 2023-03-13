num = input("Введите числа:")
num = [int(x) for x in num.split()]
length = len(num)
if length == 1:
    print("Нет")
elif num == list(range(num[0], num[-1] + 1)):
    print("Да")
else:
    print("Нет")