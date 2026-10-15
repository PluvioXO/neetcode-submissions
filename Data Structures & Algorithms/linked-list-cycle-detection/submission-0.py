# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            sp = head
            fp = head.next.next
        except:
            return False 
        while fp != None or sp!= None:
            if id(sp) == id(fp):
                return True
            try:
                sp = sp.next
                fp = fp.next.next
            except:
                return False 
        return False 