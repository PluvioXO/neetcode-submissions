# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None: 
            return True
        stack = [[root, [-1001, 1001]]]
        while len(stack) > 0: 
            item = stack.pop() 
            if item[0].val > item[1][0] and item[0].val < item[1][1]:
                if item[0].right != None:
                    stack.append([item[0].right, [item[0].val, item[1][1]]])
                if item[0].left != None: 
                    stack.append([item[0].left, [item[1][0], item[0].val]])
            else:
                return False
        return True
