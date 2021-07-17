def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[12,13,14,15,16,78,89,90]
even,odd=count(lst)
print(even)
print(odd)
print(f"Even numbers count is {even} and odd numbers count is {odd}")
print("Even numbers count is {} and odd numbers count is {}".format(even,odd))

x=9
y=10
print(f"My brothers age is {x} and my age is {y}")
print("My brothers age is {} and my age is {}".format(x,y))

#using various string functions
a="SHALU"
c="!!!!!!Tanvi!!!!"
print(c.lstrip(" "))#removing any character from left side fo the string
print(c.rstrip("!"))#removing any character from right side fo the string
print("After striping TANVI is like this- ",end = "")
print(c.strip("!"))#removing any character from both side fo the string
#print(c)
print(a.islower())#checks if the string is in lower case
print(a.isupper())#checks if the string is in upper case
a="pankaj"
print(a)