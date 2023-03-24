def answ(question):
    question = question.lower()
    trener = question.find('трен')
    rasp = question.find('расп')
    oplat = question.find('оплат')
    kaplan = question.find('каплан')
    if trener != -1:
        print_trener()
    elif rasp != -1:
        print_rasp()
    elif oplat != -1:
        print_oplat()
    elif kaplan != -1:
        print_kaplan()
    else:
        print_error()

def print_trener():
    print('Контактные данные тренера:\nТелефон: +7123456789\nПочта:Trener1337@sexy.ru')
def preint_rasp():
    print('Расписание:\nОП ОП ОП ОП ОП')
def print_oplat():
    print('к оплате:\nДуши студентов')
def print_kaplan():
    print('поздравляю! Вы нашли секретный запрос')
def print_error():
    print('Ты тупой, иди отсюда')
