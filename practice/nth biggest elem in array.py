a = [23, 23, 45, 46, 47, 49, 49, 49, 50, 50]
b = []
n = 3

a.sort()
#removes duplicates
for i in range(len(a)):
    temp = a[i]
    if temp not in b:
        b.append(temp)


if n > len(b):
    print(-1)
else:
    print(b[len(b) - n])
