# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrderTraversal = [] 
        if root == None:
            return 0
        treeOrdered = [] 
        def inOrder(item: TreeNode): 
            if item.left != None:
                inOrder(item.left)

            inOrderTraversal.append(item.val)

            if item.right != None: 
                inOrder(item.right)
        
        inOrder(root) 
        return(inOrderTraversal[k-1])




            