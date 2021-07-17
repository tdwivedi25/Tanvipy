import collections
import logging
import datetime
import re
import xml.etree.ElementTree as ET

data='''
<notes>
    <note>
      <to>Tove</to>
      <from>Jani</from>
      <heading>Reminder</heading>
      <body>Don't forget me this weekend!</body>
    </note>
</notes>
<notes>
    <note>
      <to>Tove1</to>
      <from>Jani1</from>
      <heading>Reminder1</heading>
      <body>Don't forget me </body>
    </note>
</notes>
'''
mytree=ET.parse("note.xml")
myroot=mytree.getroot()
print(myroot.tag)
print(myroot[0].tag)
print(myroot[0].attrib)

for x in myroot[0]:
    print(x.tag, x.attrib)
for x in myroot[0]:
    print(x.text)

#myroot=ET.fromstring(data)
print(myroot.tag)


a="1.2"

result=re.search('[+-]?[0-9]+\.[0-9]+', a)
if result:
    print("floating point number")
else:
    print("not afloating number")


list1=[]
for i in range(9):
    #print(bin(i))





    list1.append(bin(i))
print(list1)

names=["td", "Id", "Td", "Id"]
print(collections.Counter(names))


import re

sentence = '''My phone number is 40899-775-4844 ,
My phone number is 40896-779-4845
'''
x=re.findall('[a-m]',sentence)
print(x)

f=re.findall('\s',sentence)
print(f)

print("*****************************************************************************************")

text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald apple: 892.345.3428 436 orange Avenue
Frank Burger: 925.541.7625 662 orange apple Way

apple Albrecht: 548.326.4584 919 orange Place"""

regex1=re.compile("orange")
res=regex1.sub("strwaberry ", text)
print(res)


regex1=re.compile("\n")
res=regex1.sub(" ", text)
print(res)



index=0
entries=re.split("\n+", text)
result=re.findall(r"orange", text)
result1=re.findall(r"apple", text )
#for m in result:
 #   print(m.start(), m.end())
#if index==-1:
 # print(entries)
#print(result)
print(collections.Counter(result))
print(collections.Counter(result1))
print("*****************************************************************************************")
z="hat rat cat mat"

regex=re.compile("[r]at")
a=regex.sub("billo", z)
print(a)

print("*****************************************************************************************")

name="Shalini DwivediTripathi"

if re.search("\w{2,20}\s\w{2,20}", name):
    print("Shalini found")
print("*****************************************************************************************")
logging.basicConfig(filename="newfile.log", format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

print("*****************************************************************************************")
a = datetime.datetime(2017, 6, 21, 18, 25, 30)
b = datetime.datetime(2017, 5, 16, 8, 21, 10)
c=a-b
print("difference in dates:", c)
print(c.total_seconds()/60)
print(c.seconds/60)

x=datetime.date.today()

print(x)
print("*****************************************************************************************")

listA=[('items1','42.00'),('items2', '34.00'),('items1','42.50'),('items4', '34.60')]
print(sorted(listA, key=lambda x: x[1]))




x="shalini"
#print(x[::-1])
reversestring=''.join(reversed(x))
#print(reversestring)
z=[]
for j in range(len(x)-1,-1,-1):
    z.append(x[j])
print(z)
print("geeks"), print("geeksforgeeks")


a = 15

# function to change a global value
def change():
    # increment value of a by 5
    global a

    a = a + 5
    print(a)


change()


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# x is a generator object
x = simpleGeneratorFun()

print(x.__next__())
print(x.__next__())
print(x.__next__())


if re.search("inform", "we need to inform them inadvance"):
    print("there is inform")


allinform=re.findall("inform", "we need to inform them inadvance")
for x in allinform:
    print(x)


allinform=re.finditer("inform", "we need to inform them in advance inform to team as well")
for x in allinform:
    y=x.span()
    print(y)