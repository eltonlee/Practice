a = int(input("Your number is: "))

for i in range(2, a):
    if a % i == 0:
        print("not prime")
        quit()
    print(" this number is prime")
