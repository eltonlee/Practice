#print all recurring values in a given list
a = [23, 23, 45, 46, 47, 49, 49, 49, 50, 50]
b = []

for i in range(len(a)):
    temp = a.pop(0)
    if temp in a and temp not in b:
        b.append(temp)

print(b)
