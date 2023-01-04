from collections import defaultdict, deque
import heapq

def solution(tickets):
    answer = []
    que = deque()

    route = defaultdict(list)
    for start, end in tickets:
        heapq.heappush(route[start], end)

    start = "ICN"
    que.append(start)

    while que:
        start = que[-1]

        if len(route[start]) == 0 or start not in route:
            answer.append(que.pop())
        else:
            end = heapq.heappop(route[start])
            que.append(end)

    return answer[::-1]

#tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
answer = solution(tickets)
print(answer)