zad = "ААААBBBCCF"
result = ""

for i in set(zad):
    number = zad.count(zad[0])
    result += str(number)
    result += zad[0]
    zad = [j for j in zad if j != zad[0]]

print(result)