import collections
#using namedtuple()
data=collections.namedtuple('text',['age','favourite_color','hobby'])#returns a tuple with names for each position in the tuple.
tup=data(11,'red','sketching')
print(tup)
print(tup.favourite_color)
tup1=data._make([25,'yellow','reading'])#to create a namedtuple instance with a list.
print(tup1)
#using OrderedDict()
dict=collections.OrderedDict()#function is similar to a normal dictionary object in Python.
dict['happy']='sad'
dict['cold']='hot'
dict['boy']='girl'
dict['push']='pull'
dict['wet']='dry'
for i,j in dict.items():
    print(i,"'s opposite is",j)
dict1={'num':'1','string':'abc','float':5.4,'color':'red'}


for x,y in dict1.items():
    print(x,':',y)

dict1['num']=300
for x,y in dict1.items():
    print(x,':',y)