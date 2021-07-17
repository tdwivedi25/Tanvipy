a = 4
b = 0
try:#tries to execute the code
    print('Resource Open.')
    print(0/b)
except Exception as e:#if the try block is not executed it goes in this block.
    print("Hey user you cannot divide 4 by 0.")
    print(e)#prints the computer error
finally:#at the end this block is executed
    print("Resource Closed.")