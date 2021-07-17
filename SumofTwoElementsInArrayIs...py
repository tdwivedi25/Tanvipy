from array import *
arr1=array('i',[1,2,3,4,5,6,7,8,9,10])
answer=int(input('Enter a number you want the addends of :'))
for x in arr1:
  for y in arr1:
    if x+y==answer:
     print(x,'+',y,'=',answer)






