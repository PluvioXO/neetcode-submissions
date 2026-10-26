# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        def search(current: Optional[TreeNode]):
            nonlocal ans; 
            left, right = 0, 0 
            if current.left != None: 
                left = search(current.left)
            if current.right != None: 
                right = search(current.right)
            ans = max(ans, left + right)
            return max(left,right)+1
        
        search(root)
        return ans;