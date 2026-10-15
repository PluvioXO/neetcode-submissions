class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        ans = []
        freq = [[] for i in range(len(nums)+1)]
        for x in nums:
            if x not in hashmap:
                hashmap[x] = 1
            else:
                hashmap[x] += 1

        for key, value in hashmap.items(): 
            freq[value].append(key)

        for i in range(len(nums), 0, -1):
            ans = ans + freq[i]
            if len(ans) == k: 
                return ans
        
        