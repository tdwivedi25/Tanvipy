def convert_in2cm(inches):
    return inches * 2.54

def convert_in2kg(pounds):
    return pounds / 2.2

height_in_inches = int(input("Enter your height in inches: "))
weight_in_pounds =  int(input("Enter your weight in pounds : "))

height=convert_in2cm(height_in_inches)
weight=convert_in2kg(weight_in_pounds)

ping_ball_tall = round(height//4)
ping_ball_weight=round(weight*1000/2.5)

feet = height_in_inches//12
feet1 = height_in_inches%12

print("You are ",feet,"feet and ",feet1,"inches tall and you weigh",weight,"kg")
print("You are ",ping_ball_tall,"ping pong balls tall and your weight is same as",ping_ball_weight,"ping pong balls!")

