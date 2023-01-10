from collections import deque
#variables
graph = []
numOfHouse = []
dr = [-1,1,0,0]
dc = [0,0,-1,1] 

#input
n = int(input())
for i in range(n):
    graph.append(list(map(int, input())))


def bfs(row, col, graph):
    answer = 0
    que = deque()
    que.append((row, col))

    while que:
        (currentRow,currentCol) = que.popleft()
        graph[currentRow][currentCol] = 0
        for index in range(4):
            nextRow = currentRow + dr[index]
            nextCol = currentCol + dc[index]
            if nextRow >=0 and nextRow < n and nextCol >=0 and nextCol < n and graph[nextRow][nextCol] == 1:
                answer += 1
                graph[nextRow][nextCol] = 0
                que.append((nextRow,nextCol))
    return answer

for row in range(n):
    for col in range(n):
        if graph[row][col] == 1:
            numOfHouse.append(bfs(row,col, graph) + 1)

numOfHouse.sort()
print(len(numOfHouse))
for house in numOfHouse:
    print(house)



