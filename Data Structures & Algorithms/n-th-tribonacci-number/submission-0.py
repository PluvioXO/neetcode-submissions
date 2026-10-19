class Solution:
    def tribonacci(self, n: int) -> int:
        memory = {0: 0, 1:1, 2:1}
        ptr = 3 
        while True:
            if n in memory:
                return memory[n]
            memory[ptr] = memory[ptr-1] + memory[ptr-2] + memory[ptr-3]
            ptr +=1