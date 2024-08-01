
from typing import List


class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cardNum = len(cards)
        odd = []
        even = []
        for card in cards:
            if card % 2 == 0:
                even.append(card)
            else:
                odd.append(card)
        odd.sort(reverse=True)
        even.sort(reverse=True)
        oddNum = len(odd)
        evenNum = len(even)
        
        ## 判断失败情况
        if oddNum % 2 == 1 and cnt == cardNum and cnt != 1:
            return 0
        
        if cnt % 2 == 1 and evenNum == 0:
            return 0
        
        evenpos = 0
        oddpos = 0
        ans = 0
        
        if cnt % 2 == 1:
            cnt -= 1
            evenpos +=1
            ans += even[0]
            
        while cnt > 0:
            if evenNum -evenpos >= 2 and oddNum - oddpos >= 2:
                if even[evenpos] + even[evenpos+1] > odd[oddpos] + odd[oddpos+1]:
                    ans += even[evenpos] + even[evenpos+1]
                    evenpos += 2
                else:
                    ans += odd[oddpos] + odd[oddpos+1]
                    oddpos += 2
                cnt -= 2
                
            elif evenNum -evenpos >= 2:
                ans += even[evenpos] + even[evenpos+1]
                evenpos += 2
                cnt -= 2
            else:
                ans += odd[oddpos] + odd[oddpos+1]
                oddpos += 2
                cnt -= 2
        return ans
    

# s = Solution()
# cards = [10]
# cnt = 1
# print(s.maxmiumScore(cards, cnt))