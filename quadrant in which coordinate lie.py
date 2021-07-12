#Find out the quadrant in which the coordinate lie
x=int(input("Enter value for x-aix:"))
y=int(input("Enter value for y-axis:"))
if x>0 and y>0:
    print('x and y lies in first quadrant')
elif x<0 and y>0:
    print('x and y are in second quadrant')
elif x<0 and y<0:
    print('x and y are in third quadrant')
elif x>0 and y<0:
    print('x and y are in fourth quadrant')
else:
    print('x and y are at origin')
