from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        if not ones1 or not ones2:
            return 0

        count = defaultdict(int)
        best = 0
        for (x1, y1) in ones1:
            for (x2, y2) in ones2:
                offset = (x2 - x1, y2 - y1)
                count[offset] += 1
                if count[offset] > best:
                    best = count[offset]

        return best