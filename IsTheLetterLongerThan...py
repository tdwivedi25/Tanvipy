import collections
length_of_list=int(input('What should be the length of the list??? '))
names=[]
for y in range(0,length_of_list):
    element=input(('Enter an element you want to add to the list: '))
    names.append(element)
print(names)

three_letter_words = []
for i in names:
 if len(i) == 3:
      three_letter_words.append(i)
print(three_letter_words)

print("The count of elemnets with 3 letters is: ",len(three_letter_words))


