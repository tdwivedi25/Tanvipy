x = 25
def display():
     x = 15
     x = globals()['x']#globals function uses the global variable(outside the function)
     print(x)
display()

y = 11
def Tanvi():
    global y#global keyword uses the local variable(inside the functiion)
    y = 9
    print(y)
Tanvi()
