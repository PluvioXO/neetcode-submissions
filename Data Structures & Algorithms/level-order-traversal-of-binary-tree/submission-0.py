# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        stack = [[root, 0]]
        while len(stack) > 0: 
            item = stack.pop()
            print(ans)
            try:
                ans[item[1]].append(item[0].val)
            except:
                ans.append([item[0].val])
            item[0].right != None and stack.append([item[0].right, item[1]+1])
            item[0].left != None and stack.append([item[0].left, item[1]+1])
        return ans