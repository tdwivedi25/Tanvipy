text=input('Enter a text :')
def vowels():
 list_of_vowels=('a','e','i','o','u')

 for x in text:
    for i in list_of_vowels:
      if x ==i :
          print('Your entered input has a vowel in it')

 else :
        print('No vowel found.')
vowels()







