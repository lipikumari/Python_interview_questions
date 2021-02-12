#we can code this with the help of 2 methods
#Methods 1
num=int(input("Enter the number:"))
n1,n2=0,1
print("Fibonacci series:",n1,n2,end=",")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")

print()
#Method 2
def fibonacciSeries(i):
    if i<=1:
        return i
    else:
        return(fibonacciSeries(i-1)+fibonacciSeries(i-2))
if num<=0:
    print("Please enter a Positive Number")
else:
    print("fibonacci Series:", end=" ")
    for i in range(num):
        print(fibonacciSeries(i), end=" ")
