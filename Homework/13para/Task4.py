file_input = input('Введите имя файла, который вам нужен: ')
slovar = {}
with open(file_input, 'r') as file:
    for line in file:
        words = line.strip().lower().split()
        for word in words:
            word = word.strip('.,!?')
            if word in slovar:
                slovar[word] += 1
            else:
                slovar[word] = 1

cheto = max(slovar, key=slovar.get)

print("Слово, которое встречается чаще всего: ", cheto)
print("кол-во этого слова в файле: ", slovar[cheto])