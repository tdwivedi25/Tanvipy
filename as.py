def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

x=fact(5)
print(x)

def facto(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
res=facto(6)
print(res)