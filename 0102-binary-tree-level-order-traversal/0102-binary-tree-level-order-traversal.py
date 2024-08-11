# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        
        
        q = []
        res = []
        q.append(root)
        while q:
            ans = []
            l = len(q)
            for l in range(l):

                current_node = q.pop(0)
                ans.append(current_node.val)
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            res.append(ans)
        
            
            
        return res