num=int(input("Enter a number:"))
sum=(num*(num+1))/2
print("The sum of n naturals number is {}".format(sum))
#method 2
num=int(input("Enter a number:"))
value=0
for i in range(1 , num+1):
    value=value+i
print("Sum of n natural numbers:",value)
