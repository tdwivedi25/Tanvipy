a = ('tanu')
print(a.capitalize())#capitalize method capitalizes the first letter of the string.

b = ('ISHAN')
print(b.casefold())#casefold converts string into lowercase
print(b.center(10,"T"))#returns the string in a centered postion.Takes two arguments.1st one is the lenght of the string.2nd one is the characters which should fill the space

x = ('My name is TANU')
print(x.count('o'))#tells the number of times a value has occured
print(x.endswith('U'))#returns a boolean value.Tells if the string ends in this value

y=('\tMy\tname\tis\tTANU')
print(y.expandtabs(20))#.It takes the argument as the no. of spaces and gives the string that no. of spaces
print(y.find('T'))#finds the value and tells at which location it is.
print('My brother\'s name is {:<} and my name is {:>}'.format(b,a))#method formats the specified value(s) and insert them inside the string's placeholder.

name_dict = {'x':'Tanvi','y': 'Dwivedi'}
print("{x}'s last name is {y} ".format_map(name_dict))#used to return an dictionary key’s value.
#one more example for format_map()
register={'names':['Tanvi','Ishan'],'age':[4,11],'schools':['Eaton Elementary','Delight Montessori']}
print("{names[0]}'s age is {age[1]} and she studies in {schools[0]}".format_map(register))
print("{names[1]}'s age is {age[0]} and he studies in {schools[1]}".format_map(register))

w = ('Tanvi133')
print(w.isalnum())#returns a boolean value and tells if it is a alphanumeric value

z = ('TanviDwivedi')
print(z.isalpha())#returns a boolean value and tells if it is a alphabet value

k =("\u0033")
print(k.isdecimal())#returns a boolean value and tells if it is a decimal value

xy =("9890561665")
print(k.isdigit())#returns a boolean value and tells if it all are digits

st=('namedict')
print(st.isidentifier())#returns a boolean value if it is a identifier
print(st.isprintable())

qr=(' ')
print(qr.isspace())#returns a boolean value if it is a whitespace

title="Hello And Welcome To Pycharm"
print(title.istitle())#returns a boolean value if it is a title

#Using join()in dictionary
data={'color':'red','dress':'skirt','food':'pasta'}
print(' $ ' .join(data))#joins $ sign at the end of each key.Takes the dictionary name as an argument
#Using join()in tuple
items=('colors','dresses','food items')
print(' @ '.join(items))#joins @ sign at the end of each item.Takes the tuple name as an argument
#Using join()in set
items1={'color','dress','food'}
print(' 1 '.join(items1))#joins 1 sign at the end of each element and rearranges the order.Takes the set name as a argument
#Using join() in list
colors=['red','yellow','blue']
print('*'.join(colors))#joins * sign at the end of each element.Takes the list name as an argument.

abc='Tanvi'
bc=abc.ljust(20)#Returns a left trim version of the string
print(bc,'is her name.')
cd=(abc.rjust(30))#Returns a right trim version of the string
print('My name.',cd)





