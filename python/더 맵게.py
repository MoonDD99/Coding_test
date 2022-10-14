import heapq
def failSolution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        answer += 1
        if len(scoville) >= 2 :
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            mix = first + (second * 2)
            if first >= K:
                return answer -1
            if mix >= K:
                return answer 
            else:
                heapq.heappush(scoville,mix)
        else :
            if heapq.heappop(scoville) >= K :
                return answer + 1
    
    return -1
def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        try:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + second * 2)
            answer += 1
        except IndexError:
            return -1
    return answer