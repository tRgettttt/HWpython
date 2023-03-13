marks = [0, 0, 0, 0, 0]
mark = int(input("Введите значение: "))

while mark != -1:
    marks[mark - 1] += 1
    mark = int(input("введите значение: "))

percent = marks[-1] / sum(marks) * 100
print("Percent of 5's is %s" % int(percent) + '%')