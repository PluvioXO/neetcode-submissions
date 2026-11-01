# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def search(current):
            nonlocal ans; 
            if current == None:
                return
            ans.append(current.val)
            if current.left != None:
                search(current.left)
            if current.right != None:
                search(current.right)
        search(root)
        return ans; 