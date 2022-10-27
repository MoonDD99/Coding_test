from itertools import combinations
from collections import Counter
def solution(orders, courses):
    answer = []
    
    for course in courses:
        combList = []
        for order in orders:
            combList += combinations(sorted(order), course)
        combCount = Counter(combList)
        if len(combCount) != 0 and max(combCount.values()) != 1:
            answer += [''.join(comb) for comb in combCount if combCount[comb] == max(combCount.values())]
    
    return sorted(answer)