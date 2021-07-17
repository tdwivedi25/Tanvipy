string1=input("enter your string: ")
print(string1)
vowels=["a","e","i","o","u"]
count=0
for char in string1:
    if char in vowels:
        count+=1
print("No of vowels in given string is: ",count)
if (count==0):
        print("no vowels")

