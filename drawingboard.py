class Solution:
    def dailyTemperatures(self, temperatures):
        count = 1
        stack = []
        for i, t in enumerate(temperatures):
            if i < len(temperatures) - 1:
                if t < temperatures[i + 1]:
                    stack.append(count)
                    count = 1
                else:
                    count += 1
                    stack.append(count)
        return stack


print(Solution.dailyTemperatures(Solution, [73,74,75,71,69,72,76,73]))
