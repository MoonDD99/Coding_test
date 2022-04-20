from itertools import combinations

"""
처음에는 삼중for문 사용해서 풀었으나
비효율적이라 생각해서 구글링을 통해 
파이썬 itertools에서 조합을 구하는 함수인 combinations가 있다는 것을 알았다.
"""


def isPrime(a,b,c):
    sum = a+b+c
    for div in range(2,sum):
        if sum % div == 0:
            return False
    return True

def solution(nums):
    #score : 100.0 /100.0
    answer = 0
    
    lst = list(combinations(nums,3))
    for three_num in lst:
        if isPrime(three_num[0],three_num[1],three_num[2]):
            answer += 1    

    return answer