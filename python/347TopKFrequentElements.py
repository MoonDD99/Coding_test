from collections import defaultdict
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

nums =[1]
k=1
answer = Solution.topKFrequent(nums,k)
print(answer)