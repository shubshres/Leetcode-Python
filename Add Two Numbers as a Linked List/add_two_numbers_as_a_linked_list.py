import math

class Node(object):
    def __init__(self, x):
        # Usually has value and a pointer to the next LL node
        # Initializer
        self.val = x
        self.next = None

class Solution:

    def addTwoNumbers(self, l1, l2):
        return self.addTwoNumbersHelper(l1, l2, 0)
    def addTwoNumbersHelper(self, l1, l2, c):
        val = l1.val+ l2.val+ c
        c = val // 10 # // is floor in python
        # c = math.floor(c)
        ret = Node (val % 10)

        if (l1.next != None or l2.next != None):
            if not l1.next:
                l1.next = Node(0)
            if not l2.next:
                l2.next = Node(0)
            ret.next = self.addTwoNumbersHelper(l1.next, l2.next, c)
        return ret


l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

answer = Solution().addTwoNumbers(l1, l2)

while answer:
  print(answer.val, end=' ')
  answer = answer.next

# Time complexity: O(n)
# Space complexity: O(n)