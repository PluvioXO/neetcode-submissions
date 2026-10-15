# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1, stack2 = [p], [q]
        while len(stack1) != 0 and len(stack2)!= 0:
            nodep = stack1.pop()
            nodeq = stack2.pop()
            if nodep == None or nodeq == None:
                if nodep == None and nodeq == None:
                    continue;
                else:
                    return False
            if nodep.val != nodeq.val:
                return False
            stack1.append(nodep.right)
            stack1.append(nodep.left)
            stack2.append(nodeq.right)
            stack2.append(nodeq.left)

        if len(stack1) == 0 and len(stack2) == 0: 
            return True
        return False 