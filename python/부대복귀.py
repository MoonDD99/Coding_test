from collections import deque,defaultdict

def solution(n, roads, sources, destination):
    answer = []
    adj = defaultdict(set) # 인접한 지역
    minDist = [[0 for _ in range(n+1)] for _ in range(n+1)] #지역별 최소거리
    
    for start, target in roads:
        adj[start].add(target)
        adj[target].add(start)
        
        minDist[start][target] = 1
        minDist[target][start] = 1
       
    def bfs(source):
        visited = [False for _ in range(n+1)]
        
        que = deque([(source,1)])
        
        while que:
            print("que : " + str(que))
            start, dist = que.popleft()
            
            print("start : " + str(start))
            print("dist : " + str(dist))
            if start == destination:
                return dist+1
            
            if not visited[start]:
                visited[start] = True
                for target in adj[start]:
                    if minDist[target][destination] >= 1:
                        minDist[start][destination] = minDist[target][destination] + dist
                        minDist[destination][start] = minDist[target][destination] + dist
                        return minDist[start][destination]
                    if minDist[start][target] != 1:
                        minV = min(minDist[start][target], dist+1)
                        minDist[start][target] = minV
                        minDist[target][start] = minV
                    else: 
                        minDist[start][target] = dist+1
                        minDist[target][start] = dist+1
                    
                    que.appendleft((target,dist+1))
        return -1
            
    for source in sources:
        answer.append(bfs(source))
    
    return answer

n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1, 3, 5]
destination = 5

result = solution(n,roads,sources, destination)
print(result)