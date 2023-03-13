price = int(input())
while price != 0:
    if price % 2 == 0:
        while price % 2 == 0:
            price /= 2
    else:
        price = round(price * 0.85, 2)
    print(f"К оплате: {price}")
    price = int(input())