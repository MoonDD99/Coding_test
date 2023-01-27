from collections import defaultdict, deque
def solution(n, wires):
    answer = 1000
    graph = defaultdict(set)

    for first, second in wires:
        graph[first].add(second)
        graph[second].add(first)
    print(graph)
    for wire in wires:
        count = bfs(n, wire[0], wire[1], graph)
        answer = min(answer, abs(n - count - count))

    return answer

def bfs(n, exceptFirst, exceptSecond, graph):
    count = 1
    visited = [False] * (n+1)
    visited[exceptFirst] = True

    que = deque()
    que.append(exceptFirst)

    while que:
        node = que.popleft()
        for nearNode in graph[node]:
            if visited[nearNode] or nearNode == exceptSecond:
                continue
            count += 1
            visited[nearNode] = True
            que.append(nearNode)
    print(str(exceptFirst) + ", " +  str(exceptSecond) + ", " + str(count))
    return count 
        
n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
answer = solution(n, wires)
print(answer)
