import sys
'''
n = int(input('What number do you want? '))
a = 1

if n == 1:
    print(True)
    sys.exit()

while a < n:
    a *= 5
    if a == n:
        print(True)
        sys.exit()

print(False)
'''

end = 25
for i in range(2, end+1):
    prime = True
    for j in range(2,i):
        if(i % j==0):
            prime = False

    if prime:
        print(i)
