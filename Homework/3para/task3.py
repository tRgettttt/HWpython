sum1 = int(input('введите сумму первого товара:'))
sum2 = int(input('введите сумму второго товара:'))
sum3 = int(input('введите сумму третьего товара:'))
if sum1 <= sum2 and sum2 <= sum3:
    print('Акция!')
    print('К оплате:', (sum1 + sum2 + sum3)//2)
elif sum3 <= sum2 and sum2 <= sum1:
    print('Акция!')
    print('К оплате:', (sum1 + sum2 + sum3)//3)
else:
    print('К оплате:', sum1 + sum2 +sum3)