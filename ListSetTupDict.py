set ={'orange','apple','pear','papaya','plum'}
set.add(11)#add function only takes 1 argument
set.update([56,10,20,30,8.2,8.2])
print(set)
y = set.pop()
print(y)
print(set)
y = set.pop()
print(y)
print(set)#pop function in set deletes a random element.
x =['mom','dad','brother','sister']
w = x.pop()
print(w)
print(x)#pop function in list deletes the last element of the list.
#Creating a dictionary with two lists
nums = [2,4,6,8,10]
names = ['shalini','pankaj','tanvi','ishan','advika']
register = dict(zip(nums,names))
#Creating a list and a dictionary inside a dictionary
print(register)
q = {1:'Java',3 :['Python','JS','C++'],4 :{0.1 :'Ruby',0.2:'C',0.3 :'Pearl'}}
print(q[4][0.3])
#Adding a new key value to an existing dictionary 'q'
q[2]='CS'
#Adding a new dictionary to an existing dictionary'q'
q[5]={'summer':'hockey','winter':'badminton','autumn':'basketball'}

print(q)
for x, p in q.items():#item function prints the keys and values in a loop
    print(x,":",p)