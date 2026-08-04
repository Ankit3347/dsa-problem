from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)

        mn = min(nums)
        mx = max(nums)

        ans = []

        for x in range(mn, mx + 1):
            if x not in s:
                ans.append(x)

        return ans