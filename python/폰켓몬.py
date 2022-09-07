def solution(nums):
    phonekemonDict = set(nums)

    return min(len(nums)//2, len(phonekemonDict))

nums = [3,1,2,3]
#nums = [3,3,3,2,2,4]
#nums = [3,3,3,2,2,2]
answer = solution(nums)
print(answer)