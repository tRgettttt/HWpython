"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""
def fast_chess():
    from time import time
    start_time = time()
    total_time = 1800
    print('Время началось! У вас есть 30 минут на все ходы.')
    while True:
        move = input('Ваш ход: ')
        if move.lower() == 'off' or time() - start_time >= total_time:
            print('До свидания!')
            break
        else:
            time_remaining = round((total_time - (time() - start_time)) / 60, 1)
        print('Осталось времени:', time_remaining, 'минут')
fast_chess()