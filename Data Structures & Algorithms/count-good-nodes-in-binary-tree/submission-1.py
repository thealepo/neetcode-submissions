# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node , maximum):
            if not node:
                return 0

            good = 1 if node.val >= maximum else 0
            maximum = max(maximum , node.val)

            left = dfs(node.left , maximum)
            right = dfs(node.right , maximum)
            return good + left + right

        return dfs(root , root.val)

