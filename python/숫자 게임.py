import heapq
def solution(A, B):
    answer = 0
    heapA = []
    heapB = []
    
    for value in A:
        heapq.heappush(heapA,-value)
        
    for value in B:
        heapq.heappush(heapB,-value)
    while heapB and heapA:
        a = -heapq.heappop(heapA)
        b = -heapq.heappop(heapB)
        if a < b:
            answer += 1
        else:
            heapq.heappush(heapB, -b)
            
    return answer