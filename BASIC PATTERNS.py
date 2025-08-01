#nested loop
n=int(input("enter the size of n"))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()

#pattern for the size of 4ele
n=int(input("enter the size of n"))
for i in range(n):
    for j in range(n):
        print(i,end=' ')
    print()
    

#right angled triangle nested loop
n=int(input("enter the size of n"))
for i in range(n):
    for j in range(i):
        print('*',end=' ')
    print()


#right angled triangle using a single for loop
for i in range(5):
    print("*" *i)

#pattern to print like square
for i in range(5):
    print("* " *5)

#to print product of i
for i in range(5):
    print(i*5)

#hollow square
n=int(input("enter the size of n"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()


#hollow spaces print diagnoal
n=int(input("enter the size of n"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()

#hollow spaces print time glass
n=int(input("enter the size of n"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or i+j==n-1:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()


#hollow spaces print reverse time glass
n=int(input("enter the size of n"))
for i in range(n):
    for j in range(n):
        if  j==0 or j==n-1 or i==j or i+j==n-1:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()


#printing name in right-angled triangle
text='shafiya'
r=len(text)
for i in range(r):
    for j in range(i+1):
        print(text[j],end=' ')
    print()

#hollow spaces print cross
n=int(input("enter the size of n"))
for i in range(n):
    for j in range(n):
        if  i==j or i+j==n-1:
            print('*', end=' ')
        else:
            print(' ',end=' '
    print()

#right-angled triangle x and y axis mirror image 
n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=' ')
    print()

#rombus right angled triangle
# n=int(input())
# for i in range(n):
#     for j in range(i):
#         print("*",end=' ')
#     print()
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=' ')
#     print()
n=5
for i in range(1,2*n):
    s=i if i<=n else 2*n-i
    for j in range(s):
         print("*", end=' ')
    print()    


#to print * in pyramid format
rows=5
for i in range(1, rows+1):
    print(' ' * (rows-i) + '*' * (2*i-1))


#pyramid
n=int(input("enter the size of n"))
for i in range(1, n+1):
    for s in range(n-i):
        print(' ',end=' ')
    for st in range(2*i-1):
        print('*',end=' ')
    print()

#pascle triangle pattern
n=int(input("enter the size of n"))
for i in range(n):
    for s in range(n-i-1):
        print(' ',end=' ')
    num=1
    for j in range(i+1):
        print(f" {num} ", end=' ')
        num= num*(i-j)//(j+1)
    print()

#without repeating a number print right-angled triangle
r=8
n=1
for i in range(1, r+1):
    for j in range(i):
        print(n,end=' ')
        n+=1
    print()
