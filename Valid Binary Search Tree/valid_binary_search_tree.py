# Data Structure
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBSTHelper(self, n, low, high):
        if not n:
            return True
        val = n.val
        if ((val > low and val < high) and
            self.isValidBSTHelper(n.left, low, n.val) and
            self.isValidBSTHelper(n.right, n.val, high)):
            return True
        else:
            return False

    def isValidBST(self, n):
        return self.isValidBSTHelper(n, float('-inf'), float('inf'))


# Test Case
#     5
#    / \
# 4   7
node = Node(5)
node.right = Node(7)
# node.right.left = Node(2)
node.left = Node(4)
print (Solution().isValidBST(node))

# Test Case #2
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(2)
print(Solution().isValidBST(node))
