from collections import Counter
#finding values in a string
str1=input('Enter a text  :  ')
a = list(str1)
print( Counter(str1))

#finding the first time a repeated element occured
str2=input(('Enter a text :  '))
z = input('Enter the value you want to find in the text  : ')
for i in str2:
    if i==z:
     x = str2.index(z)
     print(i,'is   first coming  at the index no.:',x)
     break


