class Solution:
    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            if c == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(b + a)
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]

# Time Complexity :  O(N)
# Space Complexity:  O(N)