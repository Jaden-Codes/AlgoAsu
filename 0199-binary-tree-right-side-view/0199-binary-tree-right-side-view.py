# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        cur = root

        queue = deque([root])

        while queue:
            l = len(queue)
            counter = 0
            for _ in range(l):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

                if counter == l-1:
                    result.append(current.val)
                counter += 1
        return result
                