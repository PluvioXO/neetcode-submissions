# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        prev = head 
        current = head.next
        prev.next = None
        while current.next != None:
            temp = current.next 
            current.next = prev 
            prev = current
            current = temp 
        current.next = prev 
        return(current) 
