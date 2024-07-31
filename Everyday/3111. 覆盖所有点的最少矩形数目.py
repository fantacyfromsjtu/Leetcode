from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        xSet = set()
        for point in points:
            xSet.add(point[0])
        xList = list(xSet)
        xList.sort()
        left  = xList[0]
        count = 1
        for x in xList:
            if x - left > w:
                count += 1
                left = x
        return count