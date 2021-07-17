import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG())

try:
   f=open("myfile","w")
   a,b =[int(x) for x in input("Enter your numbers: ").split()]
   logging.info("Division by zero")
   c=a/b
   f.write("writing %d into file" %c)
except ZeroDivisionError:
    print("division by zero not allowed")
    print("Please enter a non zero number")
    logging.error("Divison by zero")
else:
    print("You have entered a nonzero number")
finally:
    f.close()
    print("file closed")
print("Code after the exception")