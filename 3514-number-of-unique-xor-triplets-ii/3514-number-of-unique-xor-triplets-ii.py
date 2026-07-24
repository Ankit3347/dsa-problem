from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        one = set()
        two = set()
        three = set()

        for x in nums:
            # Build 3-element XORs
            for v in list(two):
                three.add(v ^ x)

            # Build 2-element XORs
            for v in list(one):
                two.add(v ^ x)

            # Triplets with repeated indices
            two.add(0)      # x ^ x
            one.add(x)

        # x^x^x = x
        three |= one

        return len(three)