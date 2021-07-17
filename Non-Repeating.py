import collections
from functools import reduce




s = "agbaccaddeeff"
#print(s[::-1])
try:
   dict1=collections.Counter(s)
   print(dict1)
   for key, value in dict1.items():
      if value==1:
         print(key,":", value)
         break
except Exception as e:
   print(e)

while s != "":
   slen0 = len(s)
   ch = s[0]
   print(ch)
   s = s.replace(ch, "")
   slen1 = len(s)
   print(slen1)
   if slen1 == slen0-1:
      print ("First non-repeating character is: ",ch)
      break
   else:
      print("No Unique Character Found!")

def binary(lst1):
   A1=[]
   for i in lst1:
      A1.append(bin(i)[2:])
   return A1

lst1=[1,2,3,4]
x=binary(lst1)
print(x)

print(~12)
print(12 & 13)

Testlist=[]
for i in range(1,101):
   if i%3==0 or i%5==0:
      continue
   print(i)

def check(x, y):
   if (sorted(x)==sorted(y)):
      print("strings are anagram")
   else:
      print("strings are not anagram")

# driver code
s1 ="listen"
s2 ="silent"
check(s1, s2)


list_new=[2,3,4,5,12]
print(list(filter(lambda x: x%2==0, list_new)))
print(list(map(lambda x: x+2, list_new)))
print(reduce(lambda x, y: x+y, list_new))


p1=[2,13,15,1,3]
print(set(p1))



def fact(n):
   if n==0:
      return 1
   return n * fact(n-1)

res=fact(5)
print(res)


def fib(n):
   a = 0
   b = 1
   print(a)
   print(b)
   for x in range(n):
      c = a + b
      a = b
      b = c
      print(c)


fib(5)

