def cylinder(radius,height=5):
    volume = 3.14*radius**2*height
    return volume
c = cylinder(4,3)  #150.72 (Position)
c = cylinder(height=4,radius=3) #113.04 (Keyword)
c = cylinder(4)  #251.20000000000002 ( Default argument)
print(c)

def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)

sum(3,4,5,8,9)