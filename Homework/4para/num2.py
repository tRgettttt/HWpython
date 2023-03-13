num = 5
razvl = input('введите (game), если хотите перейти в раздел развлечений, (off - завершить)\n').lower()
if razvl == 'game':
    print('запущена игра угадай число')
    while True:
        tru = int(input('введите число:'))
        if tru == num:
            print('Вы выиграли билеты на концерт!')
            break
        elif tru is not num:
            print('попробуйте еще раз:')
if razvl == 'off':
    print('пока, пока!')