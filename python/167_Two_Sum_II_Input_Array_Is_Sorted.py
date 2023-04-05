class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = []
        for index, value in enumerate(numbers):
            left = index + 1
            right = len(numbers)-1
            while left <= right:
                mid = (left + right) // 2
                if (numbers[mid] + value) == target:
                    return[index+1,mid+1]
                elif (numbers[mid] + value) < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDict = {}

        for index, value in enumerate(numbers):
            if value in numDict:
                return [numDict[value]+1,index+1]
            else:
                numDict[target-value] = index