from collections import Counter

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        stack = []
        seen = set()

        for ch in s:
            freq[ch] -= 1

            if ch in seen:
                continue

            while (
                stack
                and stack[-1] > ch
                and freq[stack[-1]] > 0
            ):
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)