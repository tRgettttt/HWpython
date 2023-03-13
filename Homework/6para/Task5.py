plenty_union = set()
plenty_intersection = set()

numberStudent = int(input())
count = 0
initial_iteration = True
while numberStudent > count:
    plenty_languege = set()

    number_language_and_stud = int(input())
    count += number_language_and_stud

    for j in range(number_language_and_stud):
        language = input()
        plenty_languege.add(language)

    if initial_iteration == True:
        plenty_intersection.update(plenty_languege)
        initial_iteration = False

    plenty_union.update(plenty_languege)
    plenty_intersection = plenty_intersection.intersection(plenty_languege)

print(f"{len(plenty_union)} - {plenty_union}")
print(f"{len(plenty_intersection)} - {plenty_intersection}")