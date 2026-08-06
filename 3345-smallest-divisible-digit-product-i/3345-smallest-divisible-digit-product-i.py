class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num):
            product = 1
            while num:
                product *= num % 10
                num //= 10
            return product

        while True:
            if digit_product(n) % t == 0:
                return n
            n += 1