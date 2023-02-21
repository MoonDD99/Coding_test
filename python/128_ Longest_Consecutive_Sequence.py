class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Runtime : 330 ms, Memory : 28.9 MB
        nums = list(set(nums))
        nums.sort()
        count = 0
        result = set()
        if len(nums) == 0:
            return 0

        prev = nums[0]
        for index in range(1,len(nums)):
            current = nums[index]
            if (prev + 1) == current:
                count += 1
            else:
                result.add(count)
                count = 0     
            prev = current
        result.add(count)

        return max(result) + 1

class Solution:
    #Runtime : 414 ms, Memory : 27.9 MB
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0

        current = 1
        longest = 1

        for index in range(1,len(nums)):
            if nums[index-1] != nums[index]:
                if (nums[index-1] + 1) == nums[index]:
                    current += 1
                else:
                    longest = max(longest, current)
                    current = 1

        return max(longest, current)