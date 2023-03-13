nastl = input('введите настольную игру:\n').lower()
spi = []
while nastl != '0':
    if nastl not in spi:
        spi.append(nastl)
    else:
        print('эта игра уже записана')
    nastl = input()