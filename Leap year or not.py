Year=int(input("Enter Year:"))
if Year%4==0:
    if Year%100==0:
        if Year%400==0:
            print("Yes,{} is leap year".format(Year))
        else:
            print("No,{} is Leap year".format(Year))
    else:
        
        print("No,{} is Leap Year".format(Year))
else:
    print("No,{}is leap year".format(Year))
