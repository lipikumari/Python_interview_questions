#GCD of two number
num1=int(input("first number:"))
num2=int(input("second number:"))
def gcdFunction(num1,num2):
    if num1>num2:
        small  = num2
    else:
        small = num1
for i in range(1, small+1):
    if(num1%i==0) and (num2%i==0):
        gcd=i
print("gcd of two numbers:{}".format(gcd))
gcdFunction(num1,num2)
