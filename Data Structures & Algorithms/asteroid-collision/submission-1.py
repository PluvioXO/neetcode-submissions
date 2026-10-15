class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for current in asteroids[1:]: 
            # collision
            stack.append(current)
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0: 
                current = stack.pop()
                prev = stack.pop()
                if abs(current) > abs(prev):
                    stack.append(current)
                elif abs(current) < abs(prev):
                    stack.append(prev)
        return stack 

        

