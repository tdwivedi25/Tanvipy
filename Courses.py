Math=eval(input("Enter your Math score:(0-100):  "))
English=eval(input("Enter your English score:(0-100):  "))
Science=eval(input("Enter your Science score:(0-100):  "))
Social=eval(input("Enter your Social score:(0-100):  "))
if(Math>=90 and Science>=90):
    print("you can opt B>E course")
elif(English>=90 and Social>=90):
    print("you can o[pt for B SC course")
else:
    print("You can opt for any other course")

