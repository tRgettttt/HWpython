num = input()
qwe = sum(map(int,str(num)))
if qwe % 3 == 0 and int(num[-1]) % 2 == 0:
    print('делится')
else:
    print('не делится')