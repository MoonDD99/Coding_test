class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height)-1

        while left < right:
            result = max(result,(min(height[left],height[right]) * (right-left)))

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        
        return result