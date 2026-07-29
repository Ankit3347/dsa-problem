from math import factorial

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1

        half_len = n // 2
        half_cnt = [c // 2 for c in count]
        mid_char = -1
        if n % 2 == 1:
            for i in range(26):
                if count[i] % 2 == 1:
                    mid_char = i
                    break

        # total distinct arrangements of the half-multiset
        total = factorial(half_len)
        for c in half_cnt:
            if c > 1:
                total //= factorial(c)

        if k > total:
            return ""

        res = []
        cnt = half_cnt[:]
        L = half_len
        full_perm = total
        remaining_k = k

        for _ in range(half_len):
            for c in range(26):
                if cnt[c] == 0:
                    continue
                perm_c = full_perm * cnt[c] // L
                if remaining_k <= perm_c:
                    res.append(chr(97 + c))
                    cnt[c] -= 1
                    full_perm = perm_c
                    L -= 1
                    break
                else:
                    remaining_k -= perm_c

        half_str = ''.join(res)
        if mid_char != -1:
            return half_str + chr(97 + mid_char) + half_str[::-1]
        return half_str + half_str[::-1]