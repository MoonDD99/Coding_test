from collections import deque

def solution(n, edges):
    #자료구조
    #adjustNodes => SET 노드 : 연결된 정점 리스트
    #dist => LIST 1번노드에서 인덱스번호 노드까지 거리를 저장한 배열
    #queue => 탐색한 노드의 인접한 노드를 넣기 
    
    answer = 0
    #코드
    #dist 모두 0으로 초기화
    dist = [0] * (n + 1)
    
    #adjst에 인접한 정점들 정리
    adjustNodes = [[] for _ in range(n+1)]
    for edge in edges:
        adjustNodes[edge[0]].append(edge[1])
        adjustNodes[edge[1]].append(edge[0])
        
    dist[1] = 1
    que = deque([1])

    #adjust 모두 돌기
    #a -> b dist[b]가 0이 아니면 dist[a] + 1
    while que:
        currentNode = que.popleft()
        for adjustNode in adjustNodes[currentNode]:
            if dist[adjustNode] == 0:
                dist[adjustNode] = dist[currentNode] + 1
                que.append(adjustNode)
    
    farNode = max(dist)
    for d in dist:
        if d == farNode:
            answer += 1
    return answer

n = 6
vertex =[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
result = solution(n, vertex)
print(result)
        