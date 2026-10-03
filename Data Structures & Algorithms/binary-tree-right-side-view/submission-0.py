# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def dfs(root, depth):
            if root == None:
                return
            if depth >= len(l):
                l.append([])
            l[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        ret = []
        print(l)
        for i in l:
            ret.append(i[-1])
        return ret