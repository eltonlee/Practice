arr = [1, 2, 3, 4, 5]
arrb = [1, 2, 3, 4, 5, 5]
arrc = []
count = 0
counts = 0
fivecount = 0

arr.sort()
arrb.sort()

if len(arr) < len(arrb):
    small = len(arr)
else:
    small = len(arrb)

i = 0
j = 0

for c in range(small):
    if arr[i] == arrb[j]:
        arrc.append(arr[i])
        i += 1
        j += 1
    elif arr[i] == 5:
        fivecount += 1
        i += 1
    elif arrb[j] == 5:
        fivecount += 1
        j += 1
    elif arr[i] < arr[j]:
        i += 1
    else:
        j += 1

print(fivecount)
print(arrc)


for i in range(len(arr)):
    for j in range(len(arrb)):
        if arr[i] == arrb[j]:
            counts += 1
            break

print(counts)
