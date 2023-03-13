cost = int(input('сумма к оплате:'))
time = int(input('укажите время:'))

if 8 <= time <=22:
    if 10 <= time <= 12:
        print(cost//2)
    if 20 <= time <= 22:
        print(cost//4)
else:
    print('Магазин закрыт!')