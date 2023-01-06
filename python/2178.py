from collections import deque
N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

def solution(graph):
    answer = 0
    #상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]


    def bfs(firstRow, firstCol, targetRow, targetCol):
        que = deque()
        que.append((firstRow, firstCol))

        while que:
            row, col = que.popleft()
            if row == targetRow and col == targetCol :
                return graph[targetRow][targetCol]
            for index in range(4):
                nextRow = row + dr[index]
                nextCol = col + dc[index]

                if nextRow < 0 or nextRow >= N or nextCol < 0 or nextCol >= M:
                    continue
                if graph[nextRow][nextCol] == 0:
                    continue
                if graph[nextRow][nextCol] == 1:
                    graph[nextRow][nextCol] = graph[row][col] + 1
                    que.append((nextRow, nextCol))

                
    answer = bfs(0,0,N-1,M-1)
    print(answer)

solution(graph)