login = input('введите логин:\n').lower()
symb = '=?*^$№@_'
choto = ''
for i in login:
    for x in symb:
        if i == x:
            choto += x
print(choto)