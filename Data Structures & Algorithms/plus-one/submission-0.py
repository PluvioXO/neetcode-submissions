class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        i = len(digits)-1
        while i >= 0: 
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else: 
                digits[i] = 0
            i -= 1
        digits.insert(0, 1)
        digits[1] = 0
        return digits