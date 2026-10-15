# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        hashtab = {}
        dummy = ListNode(0, None)
        p1 = head
        i = 0
        while p1 != None:
            hashtab[i] = p1 
            i += 1
            p1 = p1.next
        l = 0 
        r = i-1
        while l < r: 
            dummy.next = hashtab[l]
            dummy.next.next = hashtab[r]
            dummy = dummy.next.next
            r -= 1
            l += 1
        if l == r:
            dummy.next = hashtab[l]
            dummy = dummy.next
        dummy.next = None
        return dummy.next

        