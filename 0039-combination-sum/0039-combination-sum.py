class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def dfs(i, subset, total):
            if total == target:
                result.append(subset[:])
                return
            
            if total > target or i >= len(candidates):
                return

            subset.append(candidates[i])
            total += candidates[i]
            dfs(i, subset, total)

            subset.pop()
            total -= candidates[i]
            dfs(i+1, subset, total)



        dfs(0, subset, 0)
        
        return result