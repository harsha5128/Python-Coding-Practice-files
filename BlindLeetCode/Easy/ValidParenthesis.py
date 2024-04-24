class Solution:
    def isValid(self, s):
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in Map.values():
                stack.append(c)
                continue
            if  not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack

solution=Solution()
s = "(){}"
print(solution.isValid(s))