from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')

        # 1. find maximal runs of '1's
        starts, ends = [], []
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                starts.append(i)
                ends.append(j - 1)
                i = j
            else:
                i += 1

        m = len(starts)
        leftGap = [0] * m
        rightGap = [0] * m
        G = [0] * m
        for idx in range(m):
            L = ends[idx - 1] + 1 if idx > 0 else 0
            R = starts[idx + 1] - 1 if idx < m - 1 else n - 1
            leftGap[idx] = starts[idx] - L
            rightGap[idx] = R - ends[idx]
            G[idx] = leftGap[idx] + rightGap[idx]

        # 2. sparse table for range-max on G
        if m > 0:
            st = [G[:]]
            k = 1
            while (1 << k) <= m:
                prev = st[-1]
                half = 1 << (k - 1)
                length = m - (1 << k) + 1
                st.append([max(prev[x], prev[x + half]) for x in range(length)])
                k += 1
            log_table = [0] * (m + 1)
            for x in range(2, m + 1):
                log_table[x] = log_table[x // 2] + 1

            def rmq(l, r):  # inclusive, 0-indexed
                k = log_table[r - l + 1]
                return max(st[k][l], st[k][r - (1 << k) + 1])
        else:
            def rmq(l, r):
                return 0

        def actual_gain(idx, l, r):
            return (min(starts[idx] - l, leftGap[idx]) +
                    min(r - ends[idx], rightGap[idx]))

        # 3. answer each query
        ans = []
        for l, r in queries:
            idx_lo = bisect_right(starts, l)       # first run with start > l
            idx_hi = bisect_left(ends, r) - 1       # last run with end < r

            gain = 0
            if idx_lo <= idx_hi:
                if idx_hi - idx_lo >= 2:
                    gain = max(gain, rmq(idx_lo + 1, idx_hi - 1))
                gain = max(gain, actual_gain(idx_lo, l, r))
                if idx_hi != idx_lo:
                    gain = max(gain, actual_gain(idx_hi, l, r))

            ans.append(total_ones + gain)

        return ans