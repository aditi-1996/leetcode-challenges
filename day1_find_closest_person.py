class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx = abs(x - z)
        dy = abs(y - z)
        if dx == dy:
            return 0
        return 1 if dx < dy else 2