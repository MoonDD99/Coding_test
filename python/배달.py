import heapq
def dijkstra(dist, node_cost):
    # score : 100.0 / 100.0
    # 다시 풀어볼 것!!
    heap = []
    heapq.heappush(heap,[1,0])

    while heap:
        node, cost = heapq.heappop(heap)
        for n,c in node_cost[node]:
            if cost + c < dist[n]:
                dist[n] = cost + c
                heapq.heappush(heap, [n,cost+c])

    return dist

def solution(N, road, K):
    answer = 0
    dist = [float('inf')] * (N+1)
    dist[1] = 0
    node_cost = [[] for _ in range(N+1)]

    for road_element in road:
        node_cost[road_element[0]].append([road_element[1],road_element[2]])
        node_cost[road_element[1]].append([road_element[0],road_element[2]])

    dist = dijkstra(dist, node_cost)
    answer = [i for i in dist if i <= K]
    return len(answer)

N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4
result = solution(N,road,K)
print(result)

