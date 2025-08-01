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

'''#ARRay operations
#program to conside list arr=[10,20,30,40]and perform insert operation and
deletion operation with 50 and 25at position 2 respectively delete 30 and traverse the array to fetech the number 25 is present
or not'''

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
    print(i, end=' ')
#searching
print("\n 25 in array?", 25 in arr)


'''program to check wheather the given string is palindrome or not
count the palindromic charcters repeated count 
str=madam
output: {'m':2, 'a':2, 'd':1}
str=malayalam'''
text= input("enter a name:")
if text==text[::-1]:
    print("Palindrome")
else:
    print("not a palindrone")
freq={}
for ch in text:
    freq[ch]=freq.get(ch,0)+1
print(freq)
