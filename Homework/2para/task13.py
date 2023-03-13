text = input('').split('@')
posl = text[0].split()[-1]
perv = text[1].split()[0]
print(posl + '@' + perv)