def fib (n):
    a = 0
    b = 1
    print(a)
    print(b)
    for y in range(n):
     c = a+b
     a = b
     b = c
     print(c)


fib(5)


