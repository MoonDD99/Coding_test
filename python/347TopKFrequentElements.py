from collections import defaultdict,Counter
import heapq
class Solution:
    def topKFrequent(nums, k):
        numCount = defaultdict(int)
        answer = []
        for num in nums:
            numCount[num] += 1
        
        sortNumCount = sorted(numCount.items(),key=lambda x:x[1],reverse=True)
        
        for index in range(k):
            num = (sortNumCount[index])[0]
            answer.append(num)

        return answer
    def topKFrequent1(nums, k):
        if k == len(nums):
            return nums
        
        numCount = Counter(nums)
        print(numCount.get)
        return heapq.nlargest(k,numCount.keys(), key=numCount.get)


nums =[1,1,1,1,2,2,2,3,3]
k=2
answer = Solution.topKFrequent1(nums,k)
print(answer)