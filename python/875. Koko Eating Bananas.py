import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            count = 0

            for pile in piles:
                count += ((pile-1)//mid) + 1
            
            if count > h:
                left = mid+1
            else:
                right = mid
        
        return left
