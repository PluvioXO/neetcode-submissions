class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # each boat can carry at limit and at most 2 people. 
        # people need to be leq limit
        people.sort()
        l,r = 0, len(people)-1
        total = 0 
        while l <= r: 

            if people[l] + people[r] <= limit:
                total += 1
                l += 1
                r -= 1 
            else:
                total += 1 
                r -= 1

        return total 