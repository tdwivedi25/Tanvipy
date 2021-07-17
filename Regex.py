import re

sentence = '''My phone number is 40899-775-4844 ,
My phone number is 40896-779-4845
'''
x=re.findall('[a-m]',sentence)
print(x)

f=re.findall('\s',sentence)
print(f)

y=list(dict.fromkeys(x))
print(y)

PhoneNumberRegex = re.search(r'\d+-\d\d\d-\d\d\d\d',sentence)
PhoneNumberRegex1 = re.findall(r'\d',sentence)
print(PhoneNumberRegex[0])
print(PhoneNumberRegex1)

m = re.match(r"(\w+)", "Isaac Newton, physicist")
print(m)

n=re.match("p",sentence)
print(n)


list1=['sd','pd','td','sd','pd','td','cd','rd']
list2=list(dict.fromkeys(list1))
print(list2)
print(sorted(list2))




list1=['sd','pd','td','sd','pd','td','cd','rd']
print(list(dict.fromkeys((list1))))


def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c)

fibonacci(5)

#0,1,1,2,3

def factorial(n):

    if n==1:
        return 1
    else:
        return n*factorial(n-1)

x=factorial(5)
print(x)




