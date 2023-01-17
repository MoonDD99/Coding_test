from collections import deque
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def solution(m,n,graph):

    answer = 0
    que = deque()
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    for row in range(n):
        for col in range(m):
            if graph[row][col] == 1:
                que.append([row, col, 0])

    while que:
        row, col, day = que.popleft()
        
        answer = max(day, answer)

        for index in range(4):
            nextRow = row + dr[index]
            nextCol = col + dc[index]
            if nextRow < n and nextCol < m and nextRow >= 0 and nextCol >= 0 and graph[nextRow][nextCol] == 0:
                graph[nextRow][nextCol] = 1
                que.append([nextRow,nextCol, day+1])

    for row in range(n):
        for col in range(m):
            if graph[row][col] == 0 :
                return -1

    return answer

print(solution(m,n, graph))