# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
traverse list by if less than, or greater than, val
'''
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def dfs(node):
            if not node.right and node.val < val:
                node.right = TreeNode(val)
                return
            if not node.left and node.val > val:
                node.left = TreeNode(val)
                return
            
            if node.val < val:
                dfs(node.right)
            else:
                dfs(node.left)

        dfs(root)
        return root