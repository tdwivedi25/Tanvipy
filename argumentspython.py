import re


def myfunc(*args):
    for arg in args:
        print(arg)

myfunc("sd",1, "pd", "td")

def myfunc1(*args, **kwargs):
    print(args)
    print(kwargs)

myfunc1("sd1", 11, x="pd1", y="pd1")




result=word.find("apple")
print(result)


def check(string):
  p=set(string)
  set1={"0","1"}
  if p==set1 or p=={'0'}or p=={'1'}:
      print("the given string is binary")
  else:
      print("not a binary")

  newset={'0','1'}
if __name__=="__main__":
    str_1 = "10110110"
    check(str_1)



def diff(li1, li2):
    li_diff=[i for i in li1+li2 if i not in li1 or i not in li2]
    print(li_diff)

li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]
print(set(li1+li2))
diff(li1, li2)

def intersection(arr1, arr2):

 result=list(filter(lambda x: x in arr1, arr2))
 print(result)
if __name__=="__main__":

  arr1 = [1, 3, 4, 5, 7]
  arr2 = [2, 3, 5, 6]
  intersection(arr1,arr2)

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




