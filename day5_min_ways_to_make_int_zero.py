class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):  # checking up to 60 is enough due to 2^60 > 1e18
            val = num1 - k * num2
            if val < 0:
                continue
            if val >= k and val.bit_count() <= k:
                return k
        return -1
