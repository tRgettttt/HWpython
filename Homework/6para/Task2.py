testList = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
printSet = set()
result = []
for i in testList:
    if type(i) == list or type(i) == set or type(i) == dict:
        result.append(i)

if result == []:
    print(True)
else:
    print(False)
print(result)