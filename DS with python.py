#LINEAR SEARCH
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
size= int(input("enter size of the array:"))
arr=[]
print("enter the elements:")
for i in range(size):
    num=int(input(f"element {i+1}:"))
    arr.append(num)
key = int(input("enter the element to search:"))
result= linear_search(arr,key)
if result!= -1:
    print(f"\n element {key} found at {result}")
else:
    print(f"\n element {key} not found in array")

# BINARY SEARCH
#array must be sorted // array is divided in to 2 seperate equilant halfs
#set low and high 0->n-1
#mid=low+high//2
#algorithm
#arr[mid]=key return mid
#arr[mid <key lowmid+1]
#arr[mid]>key high mid-1
#not found return -1
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    
    return -1
size=int(input("enter the size of array:"))
arr=[]
print("enter the elements:")
for i in range(size):
    num=int(input(f"element {i+1}:"))
    arr.append(num)
key=int(input("enter the element top search:"))
result= binary_search(arr,key)
if result!=-1:
    print(f"element {key} found at {result}")
else:
    print(f"\n element {key} not found in the array")

#JUMP SEARCH
#ALGORITHM
#1.Size n/sorted
#2.create a block key
#3.search operation will be performed
#arr[m]<var/key <arr(k+1)[m]
#4.compare each jump linearly

import math
#time complixity
#O(sqrt(n))
def jump_search(arr,target):
    if not arr:
        return -1
    n=len(arr)
    step=int(math.sqrt(n))
    prev=0
    while prev <n and arr[prev]<target:
        prev+=step
    for i in range(max(0,prev-step),min(n,prev+1)):
        if arr[i]==target:
            return i
    return -1
arr=[1,3,5,7,8,9,11]
target=7
result=jump_search(arr,target)
print(f"element {target} found at index {result}")

import math
def jump_search(arr,target):
    if not arr:
        return -1
    n=len(arr)
    step=int(math.sqrt(n))
    prev=0
    while prev<n and arr[prev]<target:
        prev+=step
    for i in range(max(0, prev- step), min(n,prev+1)):
           if arr[i]==target:
                return i
    return -1
arr=[1,3,5,7,8,9,11]
target=7
result=jump_search(arr,target)
print(f"element {target} found at index:{result}")

#EXPO_SEARCH
#sorted numbers searching
#check the array !=0m
#check the first element
#find the range using expo
#'''while for boundary
   #identify within boundary'''
#range perform binary search
#return result
def bsearch_range(arr,target,left,right):
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left= mid+1
        else:
            right= mid-1
def expo_search(arr,target):
    if not arr:
        return -1
    if arr[0]==target:
        return 0
    n=len(arr)
    i=1
    while i<n and arr[i]<= target:
        i *=2
    return bsearch_range(arr,target,i//2,min(i,n-1))    
arr=[2,4,6,8,10,12,14]
target=10
result= expo_search(arr,target)
print(f"element {target} found at index: {result}")

#FIBONACCI search
def fibsearch(arr,target):
    if not arr:
        return -1
    n=len(arr)
    fib2=0
    fib1=1
    fib=fib1+fib2
    while fib<n:
        fib2=fib1
        fib1=fib
        fib=fib1+fib2
    offset=-1
    while fib>1:
        i=min(offset+fib2,n-1)
        if arr[i]==target:
            return i
        elif arr[i]<target:
            offset=i
            fib=fib1
            fib1=fib2
            fib2=fib-fib1
         else:
            fib=fib2
            fib1=fib1-fib2
            fib2=fib-fib1
    if fib==1 and offset+1<n and arr[offset+1]==target:
        return offset+1
    return -1
arr=[2,4,6,8,10,12]
target=12
result=fibsearch(arr,target)
print(f"Element {target} found at index: {result}") 

#selection
#insertion
#bubble
#quick
#counting
#radix
#heap
#selection sort
'''-select min value
   -swap with min index value
   -check next min value and swap with i[0]+1
   -repeat until array comes in descending value
   *start from the first element in the list/array
   *arr[0]=min
   *compare with remaining elements to find real minimum value
   *perform swapping with current position
   *repeat the same with adding positional values for each,min check'''
'''PSEUDO CODE
   for ->0 to n-1:
   min=i
   for j -> i+1 to n:
       if arr[j]<arr[min]
       swap
   min=i+1'''
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
             if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr=[17,10,4,55]
selection_sort(arr)
print(arr)

#ascending order
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
             if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
size=int(input())
arr=[]
print(size)
for _ in range(size):
    num=int(input())
    arr.append(num)
result=selection_sort(arr)
print(result)

#descending order
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
             if arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
size=int(input())
arr=[]
print(size)
for _ in range(size):
    num=int(input())
    arr.append(num)
result=selection_sort(arr)
print(result)

#INSERTION SORT
''' * start from second element (i=1)
    * previous index valued element check
    * shift larger element one position to the right
    * insert current element in the correct position
    * will repeat the process until sorted array '''
#PSEUDO CODE
''' for i->1 to n-1:
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key'''
#INSERTION SORT
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
size=int(input())
arr=[]
print(size)
for _ in range(size):
    num=int(input())
    arr.append(num)
result=insertion_sort(arr)
print(result)

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
size=int(input())
arr=[]
print(size)
for _ in range(size):
    name=input()
    arr.append(name)
result=insertion_sort(arr)
print(result)

#'''perform insertion sort on strings based on length of the words'''
def insertion_sort_by_length(words):
    for i in range(1, len(words)):
        key = words[i]
        j = i - 1
        while j >= 0 and len(words[j]) > len(key):
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = key
words = ["apple","cherry","banana"]
insertion_sort_by_length(words)
print(words)

#'''python to hnopty'''
def insertion_sort_string(s):
    ch = list(s)
    for i in range(1, len(ch)):
        key = ch[i]
        j = i - 1
        while j >= 0 and ch[j] > key:
            ch[j + 1] = ch[j]
            j -= 1
        ch[j + 1] = key
    return ''.join(ch)
word = "shafiya"
sorted_word = insertion_sort_string(word)
print(sorted_word)

#COUNTSORT
def csortString(s):
    count=[0]*26
    for char in s:
        count[ord(char)-ord('a')]+=1
    sorted_str=''
    for i in range(26):
        sorted_str+=chr(i+ord('a'))*count[i]
    return sorted_str
name=input("enter a single word")
sorted_name=csortString(name)
print("original string:",name)
print("sorted string:",sorted_name)

'''RADIX SORT'''
''' 1. find the max num to determine number of digits
    2. set 10^0,for digit position 
    3. increment digit position,w.r.t pass 
    4. loop -> maxnum//exp>0 
    perform count sort based on current digit (num//exp)%10
    5.multiply exp by 10'''

def count_sort(arr, exp):
    n = len(arr)
    output = [0] * n 
    count = [0] * 10  
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        count_sort(arr, exp)
        exp *= 10
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Before sort:", arr)
radix_sort(arr)
print("After sort:", arr)


#linkedlist 
#insert at begin
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iab(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
        print(f"{data} inserted from begin.")
    def display(self):
        current = self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data, end='---')
            current=current.next
        print("None")

ll=LinkedList()
while True:
    print("\n LinkedList- Insert At Begin....")
    print("1. Insert")
    print("2. Display")
    print("3. Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iab(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        print("Exit the operation...")
        break
    else:
        print("Enter only ... 1/2/3")

#linkedlist 
#insert at end
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            print(f"{data} imserted at end /will be first node")
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode
        print(f"{data} inserted at end / will be the last node")
    def display(self):
        current = self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data, end='---')
            current=current.next
        print("None")

ll=LinkedList()
while True:
    print("\n LinkedList- Insert At end....")
    print("1. Insert")
    print("2. Display")
    print("3. Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iae(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        print("Exit the operation...")
        break
    else:
        print("Enter only ... 1/2/3")


#linkedlist find middle element
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None
ll = LinkedList()
elements = [4, 3, 2, 6, 5, 8, 1, 0, 12, 81]

for elem in elements:
    ll.append(elem)
print("Middle element is:", ll.find_middle())


# linkedlist deleting by value
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode    
    def deletevalue(self,key):
        current=self.head
        if not current:
            print("empty ll")
            return
        if current.data==key:
            self.head=current.next
            print(f"{key} delete from the list")
            return
        prev=None
        while current and current.data!=key:
            prev=current
            current=current.next
        if not current:
            print(f"{key} not found in ll")
            return
        prev.next=current.next
        print(f"{key} deleted from the ll")
    def display(self):
        current = self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data, end='---')
            current=current.next
        print("None")

ll=LinkedList()
while True:
    print("\n LinkedList- Insert At Begin....")
    print("1. Insert")
    print("2. Display")
    print("3. delete by value")
    print("4.exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iae(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        key=int(input("enter the value ,you want to delete:"))
        ll.deletevalue(key)
    elif choice=='4':
        print("Exit the operation...")
        break
    else:
        print("Enter only ... 1/2/3/4")


# linkedlist delete at begin
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode    
    def deletebegin(self,key):
        if self.head is None:
            print("empty=ll")
        else:
            print("deleted node from begining:",self.head.data)
            self.head=self.head.next
    def display(self):
        current = self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data, end='---')
            current=current.next
        print("None")

ll=LinkedList()
while True:
    print("\n LinkedList- Insert At Begin....")
    print("1. Insert")
    print("2. Display")
    print("3. at begin")
    print("4.exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iae(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
       ll.deletebegin(key)
    elif choice=='4':
        print("Exit the operation...")
        break
    else:
        print("Enter only ... 1/2/3/4")

  # linkedlist delete at end
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def iae(self, data):  
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode    
    def deleteend(self):  
        if self.head is None:
            print("Linked List is empty")
        else:
            current = self.head
            while current.next.next:
                current = current.next
            print("Deleted node from end:", current.next.data)
            current.next = None
    def display(self):
        current = self.head
        if not current:
            print("Linked List is empty")
            return
        while current:
            print(current.data, end=' ---> ')
            current = current.next
        print("None")
ll = LinkedList()
while True:
    print("\n--- LinkedList Operations ---")
    print("1. Insert at End")
    print("2. Display")
    print("3. Delete at End")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter a value to insert: "))
        ll.iae(data)
    if choice == '2':
        ll.display()
    if choice == '3':
        ll.deleteend()
    if choice == '4':
        print("Exiting the operation...")
        break

#### ATM Transaction
class Transaction:
    def __init__(self,transaction_type,amount):
        self.type=transaction_type
        self.amount=amount
        self.next=None
class TransactionHistory:
    def __init__(self):
        self.head=None
    def add_transaction(self,transaction_type,amount):
        nn=Transaction(transaction_type,amount)
        if not self.head:
            self.head=nn
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=nn
        print(f"{transaction_type} of Rs.{amount} recorded....")
    def show_history(self):
        if not self.head:
            print("No Transaction found")
            return 
        print("\n Transaction History ")
        current=self.head
        count=1
        while current:
            print(f"{count},{current.type}-RS{current.amount}")
            current=current.next
            count+=1
history=TransactionHistory()
while True:
    print("\n--------ATM Transaction menu-------")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.History")
    print("4.Exit")
    choice=input("enter your choice:")
    if choice=='1':
        amount=float(input("enter amount to deposit:"))
        history.add_transaction("Deposit:",amount)
    elif choice=='2':
        amount=float(input("enter amount to withdraw:"))
        history.add_transaction("WithDraw:",amount)
    elif choice=='3':
        history.show_history()
    elif choice=='4':
        print("End of transaction.....Exit!!!")
        break
    else:
        print("choose 1/2/3/4 only.....")


#consider a single linked list with insert at end nodes after insertion reverse the nodes  to print 
#the input must be 11-22-33-44-55-null     and ouput must be  55-44-33-22-11-null
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node 
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev 
    def print_formatted(self):
        temp = self.head
        while temp:
            print(temp.data, end="-")
            temp = temp.next
        print("null")
input_str = "11-22-33-44-55-null"
values = input_str.strip().split('-')
values = [val for val in values if val.lower() != 'null'] 
ll = SinglyLinkedList()
for val in values:
    ll.insert_end(int(val))
ll.reverse()
ll.print_formatted()
