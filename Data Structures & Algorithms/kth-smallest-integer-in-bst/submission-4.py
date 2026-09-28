# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
''' rv array, inorder traversal + append to rv, return index k+1 '''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rv = []

        def inorder(node):
            if not node: return

            inorder(node.left)
            rv.append(node.val)
            inorder(node.right)

        inorder(root)
        return rv[k-1]