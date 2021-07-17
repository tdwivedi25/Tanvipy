#Swaping variables in Python
#1st method using 'temp' variable
s = [1.2,2.3,3.4,4.5]
b = {1,3,5,7,9}
temp = s
s = b
b = temp
print('s =',s)
print('b =' ,b)
#2nd method using adding and subtracting
a = 12
b = 13
a = a+b #25
b = a-b #12
a = a-b #13
print('a =',a)
print('b =',b)
#3rd method
a,b = b,a
print('a =',a)
print('b =',b)
#Using Bitwise operator-and (&)
print(12 & 13)
print(26&16)
print(54&64)
#Using Bitwise operator-or(|)
print(20|10)
print(28|27)
print(32|2)
#Using Bitwise operator-XOR(^)
print(20^10)
print(35^30)
print(50^40)



