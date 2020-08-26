for i in range(1, 21):
    print i

list = []
for i in range(1, 1000001):
    list.append(i)
print list

print min(list)
print max(list)
print sum(list)

for i in range(1, 21, 2):
    print i

for i in range(3, 31, 3):
    print i

list2 = [value ** 3 for value in range(1, 11)]
for i in list2:
    print i