#LCM of two numbers
# Basically the LCM of two numbers is the smallest number which can divide the both numbers equally. This is also called Least Common Divisor or LCD.
#Program
num1=int(input("Enter the  first number:"))
num2=int(input("Enter the second number:"))
def lcmFinder(num1, num2):
    if num1>num2:
        larger=num1
    else:
        larger=num2
    while True:
        if(larger%num1==0) and (larger %num2==0):
            lcm=larger
            break
        larger=larger+1
    print("LCM of two numbers:{}".format(lcm))
lcmFinder(num1 , num2)
