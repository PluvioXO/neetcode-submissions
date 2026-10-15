# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the dummy, builder pattern. 
        dummy = builder = ListNode()
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val <= l2.val:
                builder.next = ListNode(l1.val, None)
                l1 = l1.next
            else:
                builder.next = ListNode(l2.val, None)
                l2 = l2.next
            builder = builder.next
        if l1 == None: 
            builder.next = l2
        else:
            builder.next = l1
        return dummy.next


