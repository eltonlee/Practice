#Logical way of doing this.
a = [1, 2, 3, 4, 5]
b = [0]*len(a) #need this
c = len(a)


for i in a:
    if c > 0:
        b[c - 1] = i
        c -= 1

print(b)

#Use this if you want 'a' and 'd' to be seperate.
#'a' is the original, 'b' is reversed
d = list(reversed(a))
print(d)

#Use this if you want just 'a' to be revered.
a.reverse()
print(a)

e = a
print(e)
