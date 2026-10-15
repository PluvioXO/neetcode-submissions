class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '(':
                stack.append(')')
            elif x == '{':
                stack.append('}')
            elif x == '[':
                stack.append(']')
            else: 
                item = stack.pop() if len(stack) > 0 else None
                if x != item:
                    return False
        if len(stack) != 0:
            return False 
        return True