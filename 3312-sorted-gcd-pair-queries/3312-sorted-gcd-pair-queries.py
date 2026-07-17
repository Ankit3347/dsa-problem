from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each number
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # exact[g] = number of pairs with gcd exactly g
        exact = [0] * (mx + 1)

        # Compute from large to small
        for g in range(mx, 0, -1):
            cnt = 0

            # Count numbers divisible by g
            for multiple in range(g, mx + 1, g):
                cnt += freq[multiple]

            pairs = cnt * (cnt - 1) // 2

            # Remove pairs already assigned to larger gcds
            for multiple in range(2 * g, mx + 1, g):
                pairs -= exact[multiple]

            exact[g] = pairs

        # Prefix sums over gcd values
        prefix = [0] * (mx + 1)
        running = 0

        for g in range(1, mx + 1):
            running += exact[g]
            prefix[g] = running

        # Answer queries
        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q))

        return ans