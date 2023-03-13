a = ('введите отзыв (off - завершить)')
print(a)
while True:
    feedback = input()
    if feedback == 'off':
        break
    print('Спасибо, ваш отзыв принят!')
print('Система предпочтений настроена!')