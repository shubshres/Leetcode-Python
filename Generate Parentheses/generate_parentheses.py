class Solution:
    def generateParenthesis(self, n):
        stack = []
        result = []

        countOpen = 0
        countClose = 0

        def scrubParenthesis(countOpen, countClose):
            if countOpen == countClose == n:
                result.append("".join(stack))
                return
            if countOpen < n:
                stack.append("(")
                scrubParenthesis(countOpen + 1, countClose)
                stack.pop()  # pop character we just added
            if countClose < countOpen:
                stack.append(")")
                scrubParenthesis(countOpen, countClose + 1)
                stack.pop()  # pop character we just added

        scrubParenthesis(countOpen, countClose)

        return result


# Time complexity: O(2^N)
# Space complexity: O(N)
