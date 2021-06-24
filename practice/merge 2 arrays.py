arr1 = [10, 12]
arr2 = [5, 18, 20]
res = []
i = 0
j = 0
arr1isSmaller = False
arr2isSmaller = False
if len(arr1) <= len(arr2):
    min = len(arr1)
    arr1isSmaller = True
else:
    min = len(arr2)
    arr2isSmaller = True

while i < min:
    if arr1[i] <= arr2[j]:
        res.append(arr1[i])
        res.append(arr2[j])
        i += 1
        j += 1
    else:
        res.append(arr2[j])
        res.append(arr1[i])
        i += 1
        j += 1


if arr1isSmaller:
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
elif arr2isSmaller:
    while i < len(arr1):
        res.append(arr1[i])
        i += 1

print(res)

#there is a much simpler way.
