# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
    def sameTree(self, firstTree, subTree):
        if not firstTree and not subTree:
            return True
        
        if firstTree and subTree and firstTree.val == subTree.val:
            return self.sameTree(firstTree.left, subTree.left) and self.sameTree(firstTree.right, subTree.right)
        else:
            return False

        