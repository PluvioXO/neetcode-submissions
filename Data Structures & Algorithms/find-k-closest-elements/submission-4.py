class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = [] 
        def findIdx(x): 
            l, r = 0, len(arr)-1
            while l <= r:
                mid  = (l+r)//2
                if arr[mid] == x:
                    return [mid, mid]
                elif arr[mid] > x: 
                    r = mid - 1 
                else:
                    l = mid + 1 
            print(l,r)
            return [r,l]
        start = findIdx(x)
        l, r = start
        if l == r: 
            l -= 1
        while k > 0: 
            if l < 0: 
                left = 10**9
            else:
                left = arr[l]
            if r > len(arr)-1: 
                right = 10**9
            else:
                right = arr[r]
            print(left,right,x)
            if abs(x-right) >= abs(x-left):
                ans.append(left)
                l -= 1 
            else:
                ans.append(right)
                r += 1
            k -= 1
        return sorted(ans); 