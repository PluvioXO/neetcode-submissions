# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -10**9 
        def search(current):
            nonlocal ans; 
            sumLeft, sumRight = 0, 0
            if current.left != None: 
                sumLeft = max(0, search(current.left))
            if current.right != None: 
                sumRight = max(0, search(current.right))
            ans = max(ans, sumRight+current.val+sumLeft)
            return max(sumLeft, sumRight) + current.val; 
        search(root)
        return ans;