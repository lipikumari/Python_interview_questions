#HCF of two numbers
num1=int(input("first number:"))
num2=int(input("second number:"))
arr=[]
if num1>num2:
    smaller=num2
else:
    smaller=num1
for i in range(1,smaller+1):
    if (num1 % i==0)and(num2 % i ==0):
        arr.append(i)
print("The HCF of given number :{}".format(max(arr)))
