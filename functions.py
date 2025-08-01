#function calling and defining
# def hi():
#     print("hello")
# hi()
#fun with parameters
def hi(name):
    print("Hello",name)
hi('shafiya')

#func with writtrn value
def add(a,b):
    return a+b
x=int(input())
y=int(input())
result=add(x,y)
print(result)

#multiplication
def mul(a,b):
    return a*b
x=int(input())
y=int(input())
result=mul(x,y)
print(result)

#default parameters/func occupied parameters
def hi(name='doraemon'):
    print("hello",name)
hi()
hi('shafiya')

# write a func that carrys and return all the arthematic operations to the main func code(+,-,*)
def arth(a,b):
    return a+b,a-b,a*b,a/b
a=int(input())
b=int(input())
result=arth(a,b)
print(result)

#def arth(a,b):
#     return a+b,a-b,a*b,a/b
# a=int(input())
# b=int(input())
# tot,diff,prod=arth(a,b)
# print("sum",tot)
# print("sub",diff)
# print("mul",prod)

#array operations
#program to consider a list arr=[10,20,30,40] and perform insert operation and delition operation with 50 and 25 at position 
#respectively and traverse the array to fetch a number 25 is present or not.''''


arr=[10,20,30,40]
#insert
arr.append(50)
arr.insert(2,25)
print(arr)
#deletion
arr.remove(30)
arr.pop()
print(arr)
#traversal
for i in arr:
    print(i,end=' ')
print("\n 25 in array",25 in arr)
