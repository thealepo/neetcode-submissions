# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
recursively
go to DFS
left
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True , 0)

            left , right = dfs(node.left) , dfs(node.right)
            left_bool , left_height = left
            right_bool , right_height = right

            balanced = left_bool and right_bool and abs(right_height - left_height) <= 1
            height = 1 + max(right_height , left_height)
            return (balanced , height)

        rv , _ = dfs(root)
        return rv