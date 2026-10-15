# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        hashTab = {0 : dummy}
        i, p1 = 1, dummy.next 
        while p1 != None: 
            hashTab[i] = p1
            i += 1
            p1 = p1.next
        i -= 1
        if i == 1:
            return None
        elif n == 1: 
            hashTab[i-n].next = None
        else:
            hashTab[i-n].next = hashTab[i-n+2]
        return dummy.next

