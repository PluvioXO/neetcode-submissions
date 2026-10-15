class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [int(tokens[0])] 
        i = 1
        while i < len(tokens): 
            try:
                stack.append(int(tokens[i]))
            except:
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(int(eval(f"{i2}{tokens[i]}{i1}")))
            print(stack, tokens[i])
            i += 1
        return stack[-1]