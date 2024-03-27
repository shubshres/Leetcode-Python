# Variables are dynamically typed
# Types are determined at runtime

n = 0
print("n = ", n)

n = "abc"
print("n = ", n)


# Can also do multiple assigments
n, m = 0, "abc"

n, m, z = 0.125, "abc", False


# Increment
n = 0
n = n + 1
n += 1
# cannot do n++ or n--

# Decrement
n = 0
n = n - 1
n -= 1
# cannot do n-- or n++

# None is null (absense of value)
n = 4
n = None
print("n = ", n)


# If Statements dont need parentheses or curly braces
n = 5
if n > 0:
    n -= 1
    print("n is positive")
elif n == 0:
    print("n is zero")
else:
    n += 1
    print("n is negative")

# Parentheses are optional
# are needed for multiline conditions however
# && is and, || is or, ! is not
if (n > 2) and (n != m) or n == m:
    n += 1

# while loops
n = 0
while n < 5:
    print(n)
    n += 1

# for loops
# looping from i = 0 to i = 4
for i in range(5):
    print(i)

# looping from i = 2 to i = 4
for i in range(2, 5):
    print(i)

# looping from i = 2 to i = 4 with step size 2
for i in range(2, 5, 2):
    print(i)

# looping from i = 4 to i = 2  down by -1
for i in range(4, 1, -1):
    print(i)

# Decimal division by default
print(5 / 2)

# Integer division
print(5 // 2)

# most languages round towards zero
# negative numbers will round down
print(-5 // 2)

# Workaround
# use decimal division and then convert to int
print(int(-5 / 2))

# Modulus
print(10 % 3)  # get the remainder of 1

# Except for negative values
print(-10 % 3)  # gets us the number 2

# fix this by using fmod
import math

print(math.fmod(-10, 3))  # this will give us -1

# more math helpers
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.pow(2, 3))  # 2^3
print(math.sqrt(4))  # square root of 4

# Max / Min Integer
float("inf")
float("-inf")
# python numbers are infinite so they never overflow

# Arrays  (called lists in python)]
arr = [1, 2, 3, 4, 5]
print(arr)

# arrays in python are dynamic by default

# arrays can be used as a stack
arr.append(6)
arr.append(7)
print(arr)

# pop the last element
arr.pop()
print(arr)

arr.insert(1, 7)  # insert 7 at index 1 <- O(n)
print(arr)

# Constant time operations
arr[0] = 0
arr[2] = 2

# initialize array of size n with default value of n
n = 5
arr = [0] * n
print(arr)
print(len(arr))

# -1 is not out of bounds, it prints out last element
arr = [1, 2, 3]
print(arr[-1])

# Indexing -2 is the second to last value, etc
print(arr[-2])

# Sublists (slicing)
arr = [1, 2, 3, 4, 5]
print(arr[1:3])  # prints out 2,3

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)
# output    1 2 3
# good for list of pairs
# number of variables must match the number of elements in the list

# Loop through arrays
nums = [1, 2, 3]
for i in range(len(nums)):
    print(nums[i])

# without index
for n in nums:
    print(n)

# enumerate will give us the index and the value
for i, n in enumerate(nums):
    # i is the index, n is the value
    print(i, n)

# loop through multiple arrays simultaenously
# with unpacking
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for (
    n1,
    n2,
) in zip(nums1, nums2):
    # n1 is from nums1, n2 is from nums2
    # this will only loop through the shortest array
    # if one array is longer than the other, it will ignore the extra elements
    # if you want to loop through all elements, use itertools.zip_longest

    # ZIP will take both of the arrays and combine them to an array of
    # pairs and we can unpack those pair values
    print(n1, n2)

# reverse an array
nums = [1, 2, 3]
nums.reverse()
print(nums)

# sort an array
arr = [3, 2, 1]
arr.sort()  # sort in asc order by default
print(arr)

# sort in reverse order
arr.sort(reverse=True)

# Sort list of strings
arr = ["abc", "def", "ghi"]
arr.sort()  # sort in alphabetical order by default
print(arr)

# Custom sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr)

# LIst Comprehension
arr = [i for i in range(5)]  # [0,1,2,3,4]
print(arr)

arr = [i + i for i in range(5)]  # [0,2,4,6,8]
print(arr)

# 2-D lists
arr = [[0] * 4 for i in range(4)]
# will build a 4x4 array

# Strings are similar to arrays
s = "abc"
print(s[0:2])  # prints out ab

# immutable however, cannot reasign values at specific index

# can update string but doing so will create a new string
s += "def"
print(s)
# any time you modify a string it is an n time operation

# Strings can be converted into integers and those intergers can be added.
print((int("123") + int("456")))
# output 579

# and numbers can be converted into strings
print(str(123) + str(456))
# output 123456

# If you need the ascii value of a char
print(ord("a"))

# can also join a list with an empty delimitor
print("".join(["a", "b", "c"]))  # abc

# Strings can be converted into arrays
s = "abc"
arr = list(s)
print(arr)
# output ['a', 'b', 'c']

# Queues (double ended queue)
from collections import deque

queue = deque()
# adding values to the right side
queue.append(1)
queue.append(2)
print(queue)  #  dequeue([1, 2])

# constant time
queue.popleft()  # remove from left side
print(queue)  # dequeue([2])

queue.appendleft(3)  # add to left side
print(queue)  # dequeue([3, 2])

queue.pop()  # remove from right side
print(queue)  # dequeue([3])

# Hash Sets
# can search them in constant time and insert values in constant time
# cant be any duplicates
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)  # {1, 2}
print(len(mySet))  # 2

# check if a value is in the set
print(1 in mySet)  # True
print(2 in mySet)  # True
print(3 in mySet)  # False

mySet.remove(2)
print(2 in mySet)  # False


# list ot set
print(set([1, 2, 3]))

mySet = {1, 2, 3}
mySet = {i for i in range(5)}  # {1, 2, 3, 4}
print(mySet)


# HashMaps (aka dictionaries)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 21
myMap["tracy"] = 23

# note cant have duplicate keys

print(myMap)  # {'alice': 88, 'bob': 21, 'tracy': 23}
print(len(myMap))  # 3

myMap["alice"] = 99
print(myMap)  # {'alice': 99, 'bob': 21, 'tracy': 23}

print("alice" in myMap)  # search if key is in map in constant time
myMap.pop("alice")  # remove key value pair
print("alice" in myMap)  # False
#                  "key": value
myMap = {"alice": 88, "bob": 21, "tracy": 23}


# can also fill like this:
myMap = {i: 2 * i for i in range(3)}  # {0: 0, 1: 2, 2: 4}
print(myMap)

# looping through map
# key value pairs
for key in myMap:
    print(key, myMap[key])

# just keys
for val in myMap.values():
    print(val)

# just values
for key in myMap.keys():
    print(key)

# go through the items of the map
for key, val in myMap.items():
    print(key, val)


# Tuples
# immutable
# can index them, but cannot modify them
# can be used as keys in a map
myTuple = (1, 2, 3)
print(myTuple[0])  # 1
print(myTuple[-1])  # 3

# cant modify them
# myTuple[0] = 0  # error

# Can be used as key for hashmap/set
myMap = {(1, 2): 3}
print(myMap[(1, 2)])  # 3

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)  # True

# lists are not hashable and cant be keys
# myMap[[1,2]] = 3 # error


# Heaps
import heapq

# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# by default  heaps in python are min heaps
# Min is always at index 0
print(minHeap[0])  # 2

while len(minHeap):
    print(heapq.heappop(minHeap))  # 2, 3, 4

# Max heap is not in python by default
# Workaround: use min heap  and multiply by -1 when push/pop
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))  # 4, 3, 2

# build heap from initial values!
import heapq

# build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))  # 1, 2, 4, 5, 8


# Functions
def myFunc(n, m):
    return n * m


print(myFunc(3, 4))  # 12


# Nested Functions.
# Good for recusion
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c

    return inner()


print(outer("a", "b"))  # abc


# can modify objects but not reassign values unless use nonlocal keyword
def double(arr, val):
    def helper():
        for i, n in enumerate(arr): # n is a copy of the value
            arr[i] *= val
        # will only modify val in the helper function 
        # val *= 2
        
        
        # this will modify the val outside the helper scope: 
        nonlocal val
        val*=2
    helper()
    print(arr,val)

nums=[1,2]
val = 3
double(nums,val)


class myClass: 
    # constructor
    def __init__(self,n): # self passed in every method of a class
        self.n = n # creating a member variable
        self.size = len(nums)
    
    # self key word required as param
    def getLength(self): 
        return self.size
    
    def getDoubleLength(self): 
        return 2*self.getLength()