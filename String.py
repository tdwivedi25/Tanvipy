import time
import calendar

str1="My World of Python!"
print(str1)
print(str1[3:])
print(str1[:])
print(str1[:9])
print(str1+" "+"is very huge.")

dict1={"Name":'SD', "Age":39,"Address":'10100 Cupertno'}
print(dict1)

tup1=("abc",24,45.69)
print(tup1)

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
localtime=time.localtime(time.time())
print(localtime)

cal=calendar.month(2020,1)
print(cal)
print(calendar.isleap(2020))

message="""Hi, My name is Tanvi,
I love my mom and dad.
I hate coronavirus.
"""
for letter in message:
    if (letter.isupper()):
        letter.lower()
    elif(letter.islower()):
        letter.upper()
    print(message)
print(ord('A'))
print(chr(102))


str="faizabad is small place"
strnew="".join(reversed(str))
print(strnew)
print(str[::-1])


x="EARTH"
y="HEART"
