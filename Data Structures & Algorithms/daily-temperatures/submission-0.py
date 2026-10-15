class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] 
        ans = [0] * (len(temperatures)-1)
        ans.insert(0, 0)
        # [30,38,30,36,35,40,28]
        i = 1
        while i < len(temperatures): 
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
            i += 1
        return ans 