#Find the area of a circle
#Area of circle = pi*radius*radius or (pi*diameter*diameter)/4
#Diameter=2*radius
#From using formula pi*r*r
from math import pi
r=int(input("Enter the radius:"))
Area = pi*r*r
print("Area of a circle :" + str(Area))
#From using formula (pi*d*d)/4
from math import pi
d=int(input("Enter the diameter:"))
Area=(pi*d*d)/4
print("Area of circle :" + str(Area))
