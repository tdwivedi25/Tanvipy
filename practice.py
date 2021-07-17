for x in 'Practice':
    if x == 'c':
        break
    print(x)

lst1=[2,6,90]
for x in lst1:
    if x%2!=0:
        print("List contains an odd numver", x)
        break
else:
    print("List does not conatin an odd number")


def inner_factorial(n):
    if (n <= 1):
        return 1;
    return n * inner_factorial(n - 1)

# mess up some answers to make it more interesting

def factorial(n):
    f = inner_factorial(n)
    if (n % 2):
        return f + 1
    return f

x=factorial(4)
print(x)