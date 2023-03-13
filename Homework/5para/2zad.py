spis = [0, 0, 0, 0, 0]
count = int(input('введите оценки:'))
while count != -1:
    spis[count -1] += 1
    count = int(input('введите оценки:'))
total = 0
for i in range(2, 5):
    total =+spis[i]
print('spis: ', end='')
for i in range(5):
    for g in range(spis[i]):
        print(i + 1, end=' ')
print("\nNumber of spis: " + ''.join(str(spis) +
      "\nAcademic performance: " + str(total / sum(spis) * 100)))