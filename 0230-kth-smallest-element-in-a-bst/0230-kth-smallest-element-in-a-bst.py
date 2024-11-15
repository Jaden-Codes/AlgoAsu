# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        storage = []
        if not root:
            return root
        def dfs(node):
            if not node:
                return 0

            if node.left:
                dfs(node.left)
            storage.append(node.val)
            if node.right:
                dfs(node.right)

            return storage
        dfs(root)
        return storage[k-1]        