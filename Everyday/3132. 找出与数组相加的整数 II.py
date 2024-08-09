import sys
from typing import List
import numpy as np

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        Nums1 = np.array(nums1)
        Nums2 = np.array(nums2)
        minx = sys.maxsize
        for i in range(len(Nums1)):
            for j in range(i+1,len(Nums1)):
                del_Num1 = Nums1.copy()
                del_Num1 = np.delete(del_Num1, i)
                del_Num1 = np.delete(del_Num1, j-1)
                
                sub =  Nums2 - del_Num1
                x = sub[0]
                all_same = np.all(sub == sub[0])
                if all_same:
                    minx = min(minx,x)
                    
        return int(minx)
s = Solution()
nums1 = [4,20,16,12,8]
nums2 = [14,18,10]
print(s.minimumAddedInteger(nums1,nums2))