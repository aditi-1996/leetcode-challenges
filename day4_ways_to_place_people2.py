import math
from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        count = 0
        for i in range(n - 1):
            yi = points[i][1]
            max_y = -math.inf
            for j in range(i + 1, n):
                yj = points[j][1]
                if yj <= yi and yj > max_y:
                    count += 1
                    max_y = yj
        return count