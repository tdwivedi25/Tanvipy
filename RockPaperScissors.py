import random
choices = [ "rock","paper","scissors"]
print("Rock crushes scissors, paper covers rock and scissors cut paper")
player = input("Do you want to pick rock, paper, scissors or quit? ")
while player!= quit:
    player.lower()
    computer = random.choice(choices)
    print("You chose: "+player + "and computer chose: "+computer+".")
    if player == computer:
        print("It was tie")
    elif player == "rock":
        if computer =="scissors":
          print("You win")
        else:
         print("computer wins")
    elif player == "paper":
        if computer == "rock":
            print("you win")
        else:
            print("computer wins")
    elif player == "scissors":
        if computer == "paper":
            print("You win")
        else:
            print("computer wins")
    else:
        print("I think there was an error")
    print()
    player =input("Would you like to play again?y/n")
    answer = input("Hit [Enter] to keep going, any other keys to exit: ")
    keep_going = (answer == "")
    print(keep_going)