text='I like Python basketball and History'
print(text.partition(','))#Returns a tuple where the string is parted into three parts.
                         # If the separator string is not found, then the 3-tuple contains the string itself followed by two empty strings.
print()
print(text.replace('like','love'))#Returns a string where a specified value is replaced with a specified value
print()
print(text.rfind('History'))#finds the element tells where did it last occur and the start point of a word.Returns -1 if the substring was not found.
print()
print(text.rindex('History'))#finds the element tells where did it last occur and the start point of a word.Throws an error if the substring was not found.
print(text.rpartition(','))#Returns a tuple where the string is parted into three parts.
                         # If the separator string is not found, then the 3-tuple contains the string itself and begins by two empty strings.
print()
print(text.rsplit('P'))#returns a list which is separated by commas after each element.
print()

x = '          Hello hi how r u,r u fine,hope everything is good           '
print(x.split())#?????
print()
print(x.strip())#removes the extra spaces from the beginning and end of the string
print()
print(x.startswith(' '))#returns a bool. value and tells whether the string starts with this value
print()
text2='Hello my name is Tanvi.\nI live in the United States.\nIn the U.S I live in Cupertino,California'
print(text2.splitlines())#Splits the string at line breaks and returns a list
print()

txt = text[::-1]#Reverses the string
print(txt)
print()
txt = text[::-2]#Reverses the string and skips 1 element at a time
print(txt)
print()
txt = text[::-3]#Reverses the string and skips 2 element at a time
print(txt)
print()
txt = text[::-4]#Reverses the string and skips 3 element at a time
print(txt)
print()