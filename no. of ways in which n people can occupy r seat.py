#Find out the no. of ways in which N people can occupy R seats
import math
N=int(input("Enter the number of students:"))
R=int(input("Enter the number of seats :"))
#factorial
nume=math.factorial(N)
deno=math.factorial(N-R)
#permutation
no_of_ways=nume//deno
#print no of ways
print('Total no. of ways are: ' + str(no_of_ways))
