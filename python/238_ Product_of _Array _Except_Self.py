class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenNum = len(nums)
        leftToRight = [1 for _ in range(lenNum)]
        result = [1 for _ in range(lenNum)]

        num = 1
        for index in range(lenNum):
            leftToRight[index] = num
            num *= nums[index]
        
        num = 1
        for index in range(lenNum-1,-1,-1):
            result[index] = leftToRight[index] * num
            num *= nums[index]
        return result