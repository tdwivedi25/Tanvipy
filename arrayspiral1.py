def printspiral(r,c,a):
    rstart=0
    cstart=0
    while (rstart<r and cstart<c):
       for i in range(cstart,c):
           print(array1[rstart][i],end=" ")

       rstart+=1

       for i in range(rstart,r):
           print(a[i][c-1],end=" ")

       r-=1
       if rstart<r:
          for i in range(c-1, (cstart-1), -1):
             print(array1[r-1][i])

       if(cstart<c):
           for i in range(r-1,rstart-1,-1):
               print(array1[i][cstart],end="")
           cstart+=1

array1=[
    ['a','b','c','d'],
    ['aa','bb','cc','dd'],
    ['ee','ff','jj','kk']


]
row=3
col=4
printspiral(row,col,array1)