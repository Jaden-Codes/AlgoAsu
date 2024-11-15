# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0


        def dfs(node, maxVal):
            if not node:
                return
            if node.val >= maxVal:
                maxVal = node.val
                self.goodNodes += 1

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
            return



        dfs(root, root.val)

        return self.goodNodes
        