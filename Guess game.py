import random
'''
colors = ["red","yellow","blue","white","grey","black"]
print(random.choice(colors))
print(random.choices(colors))
num_tries=1
the_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
print(the_number)
while guess != the_number:
    if guess > the_number:
      print(guess, "was too high. Try again.")
    if guess < the_number:
      print(guess, "was too low. Try again.")
    guess = int(input("Guess again: "))
print(guess, "was the number! You win!")
num_tries=num_tries+1
print(num_tries)
'''


random_num=random.randint(1,59)
print(random_num)
true_num=int(input("enter your guess between 1 to 59: "))

while true_num!=random_num:
 if true_num>random_num:
    print("guessed is higher. Try again")

 elif true_num <random_num:
     print("guessed is lower. Try again")

 true_num = int(input("guess again: "))
print(true_num, "was the number! You win!")

print(hex(23))
