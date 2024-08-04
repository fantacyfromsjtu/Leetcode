from typing import List


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        maxDis = []
        for i in range(len(points)):
            maxDis.append([max(abs(points[i][0]), abs(points[i][1])),s[i]])
            
        maxDis.sort(key=lambda x: x[0])
        met = set()
        curd = 0
        ans = 0
        accum = 0
        for point in maxDis:
            if point[0] != curd:
                ans += accum
            if point[1] in met:
                return ans
            if point[0] == curd:
                accum += 1
                met.add(point[1])
            else:
                accum = 1
                met.add(point[1])
                curd = point[0]
            
        return ans + accum
            
# points = [[-1,-4],[16,-8],[13,-3],[-12,0]] 
# s = "abda"
# sol = Solution()
# print(sol.maxPointsInsideSquare(points,s))
            
        