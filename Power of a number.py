#Find power of a number
#Method 1
base=int(input("enter base number:"))
expo=int(input("Enter expo number:"))
temp=1
for i in range(0,expo):
    temp=temp*base
print(temp)
#Method 2
base=int(input("Enter base number:"))
expo=int(input("Enter expo number:"))
base=base**expo
print(base)

