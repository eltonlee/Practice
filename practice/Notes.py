# -------------Arrays----------

# Initalize a array of size k with n stuff inside it
a = ['n']*len(k)

# Loop backwards
for i in range(len(something)-1, -1, -1)  # range (start, stop before, step)

# sort the array from lowest to highest
a.sort()
# sort the array from highest to lowest
a.sort(reverse=True)

# Set removes all duplicates in a array.
a = set(a)  # [1, 1, 2 ,3] will then be [1, 2, 3]

# finding sum of a array
sum(a)

# using map to multiply 2 arrays
a = [1, 2, 3]
b = [3, 2, 1]
c = map(operator.mul, a, b)
print(list(c))
# we get c = [3, 4, 3]

# using enumerate in a loop gives a it index and its value.
for i, num in enumerate(nums):  # i is the index and num is the value.

    # if you want to compare current element with next element without going out of bound:
for i in range(len(nums) - 1):
    # compare i and i + 1

    # -------------Strings --------------

    # To replace a character
str = str.replace('a', '')  # in this case, it is the character a

# to combine a array of strings with something or nothing
list1 = ['1', '2', '3', '4']
s = '-'
s = s.join(list1)  # result is 1-2-3-4

# to sort a string
s = ''.join(sorted(s))  # s is 'bca' but now it is 'abc'

# to reverse a string
s = ''.join(reversed(s))

# To see if a character in a string is a letter
s.isalpha()

# To see if a character in a string is a number
s.isdigit()

# convert a string to all lower case or uppercase:
s = s.lower(),   s = s.upper()

# -------------Dictionary---------------------

# To initialize a dict
d = {'a': 0, 'b': 1}

# to get a value from a key
res = d.get('a')  # 'a' is the key in this case

# to print out all values of a dictionary
for val in dic.values()
print(val)
