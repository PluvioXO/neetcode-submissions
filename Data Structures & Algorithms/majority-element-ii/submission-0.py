class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        boundary = len(nums)//3
        result = set()
        record = {}
        for item in nums: 
            if item not in record:
                record[item] = 0 
            record[item] += 1
            if record[item] > boundary:
                result.add(item)
        return list(result)