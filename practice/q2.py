from collections import Counter

k = 2
numbers= [3, 3, 3, 2]


def haha(k, numbers):
	if len(numbers)%k != 0:
		return 'No'

	

	x = Counter(numbers)
	for i in x:
		if x[i] > len(numbers)/k:
			return 'No'

	return "Yes"
	


print(haha(k , numbers))




	

