text=input('Enter a text : ')
x  = text[::-1]
keep_going=True
if text==x:
    print(x,'is the reversed version of the text given.')
    print(text,'is a palindrome.')
else:
    print(text,'is not a palindrome.Try another one.')
    keep_going