# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        ans = 0
        stack = [[root, 1]]
        while len(stack) > 0:
            item = stack.pop()
            ans = max(item[1], ans)
            item[0].right != None and stack.append([item[0].right, item[1]+1])
            item[0].left != None and stack.append([item[0].left, item[1]+1])
        return ans