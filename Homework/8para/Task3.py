"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

Ученикам без допуска должно печататься "Вы отчислены".

Выдачу допуска реализуй как функцию.
"""
def zachet(point:int):
    return point > 50

amount = int(input('Кол-во студентов: '))
for i in range(amount):
    point1 = int(input('Баллы за тест: '))
    total = zachet(point1)
    if total:
        print('Зачет')
    else:
        print('Отчислен')