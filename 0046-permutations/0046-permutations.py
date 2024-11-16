class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(start):
            if start >= len(nums):
                result.append(nums.copy())
                return

            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtracking(start + 1)
                nums[i], nums[start] = nums[start], nums[i]



        backtracking(0)

        return result
        