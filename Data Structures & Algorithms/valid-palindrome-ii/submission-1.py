class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper function to check if a substring is a perfect palindrome
        def check_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                # Mismatch found: check if skipping left OR skipping right works
                return check_palindrome(l + 1, r) or check_palindrome(l, r - 1)
            
            l += 1
            r -= 1
            
        return True