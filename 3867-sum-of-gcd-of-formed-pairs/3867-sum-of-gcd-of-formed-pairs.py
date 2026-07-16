from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)

        # Step 1: Construct prefixGcd array
        prefixGcd = []
        mx = 0

        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))

        # Step 2: Sort the array
        prefixGcd.sort()

        # Step 3: Form pairs and compute the sum of GCDs
        ans = 0
        left = 0
        right = n - 1

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans