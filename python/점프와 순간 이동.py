def solution(n):
    #scroer : 100.0 / 100.0

    """
    
    1. 2로 나누면서 나머지가 1일 경우수를 구한다
    2. 경우수에 1을 더한다.

    """
    ans = 0
    
    while n // 2 > 0:
        a,b = divmod(n,2)
        n = a
        ans += b
        
    return ans + 1

n = 5000
ans = solution(n)
print("ans : ", ans+1)