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


