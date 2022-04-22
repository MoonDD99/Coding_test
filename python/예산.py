from itertools import combinations
"""
<Problem>
1. 제한선이 정해져 있음
2. item의 합계가 제한선을 넘지 않아야함
3. item의 갯수를 최대로 해야함

<Solution>
1. item의 순서를 정렬한다.
2. 제한선보다 작아질때까지 item을 큰값부터 pop한다.
3. item의 갯수를 반환한다.
"""
def solution(d, budget):
    #score : 52.2 / 100.0
    #시간초과 발생
    answer = 0
    for index in range(len(d),0,-1):
        cases = list(combinations(d,index))
        for case in cases:
            if sum(case) <= budget:
                answer = index
                return answer
        
    return answer

def solution1(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop()
    
    return len(d)