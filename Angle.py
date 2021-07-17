hour=int(input("Enter the hour: "))
min=int(input("Enter the minute: "))
hrangle=hour*30+min*(30/60)
minangle=min*6
result=0.0
if hrangle>minangle:
    result=hrangle-minangle
else:

    result=minangle-hrangle
if result>180:
    print("the least angle is: ",360-180)
else:
    print("The angle is:", result)

