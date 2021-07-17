string1=input("enter string 1: ")
string2=input("enter string 2: ")
string1_sort=sorted(string1)
string2_sort=sorted(string2)
if (len(string1_sort)==len(string2_sort)):
     if (string1_sort==string2_sort):
        print("the strings are anagram")
     else:
        print("the strings are not anagram")
else:
    print("strings lengths are not equal")



product=1

for i in range(5,1,-1):
    print(i)