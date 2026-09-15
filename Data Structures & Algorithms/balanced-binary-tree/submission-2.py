# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True , 0)
            
            left_bool , left_height = dfs(node.left)
            right_bool , right_height = dfs(node.right)
            balanced = (left_bool and right_bool and abs(left_height - right_height) <= 1)

            return (balanced , 1 + max(left_height , right_height))

        rv , _ = dfs(root)
        return rv