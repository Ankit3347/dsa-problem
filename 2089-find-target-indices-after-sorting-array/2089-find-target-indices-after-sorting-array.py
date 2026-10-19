class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] ==target:
                res.append(i)
        return res
        