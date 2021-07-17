school_age = eval(input("What is the right age to go to school?"))
your_age = eval(input("What is your age?"))
if your_age >= school_age:
    print("You can go to school !")
else:
    print("I am sorry you cannot go to school but you will be in ",school_age - your_age)
