# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r1, r2) -> bool:
            stack1, stack2 = [r1], [r2]
            while len(stack1) > 0 and len(stack2) > 0:
                item1 = stack1.pop()
                item2 = stack2.pop()
                if item1.val != item2.val:
                    return False
                item1.right != None and stack1.append(item1.right)
                item2.right != None and stack2.append(item2.right)
                item1.left != None and stack1.append(item1.left)
                item2.left != None and stack2.append(item2.left)
            if len(stack1)+len(stack2) > 0:
                return False
            return True 
        stack = [root]
        while len(stack) > 0:
            item = stack.pop()
            if item.val == subRoot.val:
                if isSame(item, subRoot):
                    return True
            item.right != None and stack.append(item.right)
            item.left != None and stack.append(item.left)
        return False 