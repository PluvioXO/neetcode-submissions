# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        store = "" 
        s1,s2 = "", ""
        def read(current): 
            nonlocal store 
            store += str(current.val) 
            if current.next != None: 
                read(current.next)
            return;

        def write(current): 
            nonlocal ptr
            if ptr == len(s3):
                return; 
            current = ListNode(s3[ptr], None)
            ptr += 1 
            #print(current.val)
            current.next = write(current.next)
            return current
        
        read(l1)
        s1 = int(store[::-1])
        store = ""
        read(l2) 
        s2 = int(store[::-1])
        s3 = s1+s2
        s3 = str(s3)[::-1]
        start = ListNode(0, None)
        ptr = 0 
        start.next = write(start)
        return start.next