"""
Напишите генератор выводящий все символы строки на печать, но только в том случае, если они являются буквами (остальные игнорируются).
"""
def kaplan(gen):
    for j in gen:
        if j.isalpha():
            yield j
for n in kaplan(gen = input()):
    print(n)
