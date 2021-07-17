import random
suit = ["club","diamond","heart","spade"]
faces = ["two","three","four","five","six","seven","eight","nine","ten","jack","king","queen","ace"
                                                                                              ""]
keep_going = True
while keep_going:
    my_suit = random.choice(suit)
    my_face = random.choice(faces)
    your_suit = random.choice(suit)
    your_face = random.choice(faces)
    print("I have ",my_face,"of",my_suit)
    print("You have ",your_face,"of",your_suit)
    print(faces.index(my_face))
    print(faces.index(your_face))
    if faces.index(my_face)>faces.index(your_face):
        print("I win")
    elif faces.index(your_face)<faces.index(my_face):
          print("you win")
    else:
        print("it was a tie")
    answer = input("Press [Enter] to continue or press any other key to exit")
    keep_going =(answer =="")