first = int(input("Enter the first number"))
second = int(input("Enter the second number"))
for i in range(first,second):
    for j in range(2, i//2):
        if i%j==0:
            break
    else:
        print("prime number ",i)
