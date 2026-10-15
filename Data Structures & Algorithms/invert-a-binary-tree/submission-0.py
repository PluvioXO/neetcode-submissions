# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        if root == None:
            return root
        while len(stack) != 0: 
            item = stack.pop()
            temp = item.left
            item.left = item.right
            item.right = temp 
            item.right != None and stack.append(item.right)
            item.left != None and stack.append(item.left)
        return root
