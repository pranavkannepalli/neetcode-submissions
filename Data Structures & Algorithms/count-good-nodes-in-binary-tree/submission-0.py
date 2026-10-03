# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.recurse(root, -101)
        #return 1 + self.recurse(root.left, root.val) + self.recurse(root.right, root.val)
    def recurse(self, root, m):
        if root == None:
            return 0
        if root.val >= m:
            return 1 + self.recurse(root.left, root.val) + self.recurse(root.right, root.val)
        return self.recurse(root.left, m) + self.recurse(root.right, m)