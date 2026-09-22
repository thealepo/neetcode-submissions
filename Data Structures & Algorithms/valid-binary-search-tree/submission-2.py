# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
start at root, check if left is less and right is greater
once you move onto root.left and root.right, make sure
to put bounds on how great and how small the values can be

                    5
                2       8
            1      4  7    10

2 must be less than 5 but greater than -inf
8 must be less than inf but greater than 5
1 must be less than 2 but greater than -inf
4 must be less than 5 but greater than 2
7 must be less than 8 but greater than 5
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node , lower_bound , upper_bound):
            if not node: return True

            if node.val <= lower_bound:
                return False
            if node.val >= upper_bound:
                return False

            return check(node.left , lower_bound , node.val) and check(node.right , node.val , upper_bound)

        rv = check(root , float('-inf') , float('inf'))
        return rv







