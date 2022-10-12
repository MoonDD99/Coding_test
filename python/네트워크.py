def failSolution(n, computers):
    answer = 0
    #node[nodeNum] = networkNum
    node = [-1] * n
    
    for row in range(0,n):
        for col in range(0,n):
            if row == col :
                continue
            if computers[row][col] == 1 and computers[col][row] == 1:
                if node[row] != -1 and node[col] != -1:
                    #이미 네트워크에 속해있는 경우
                    continue
                elif node[row] != -1 or node[col] != -1:
                    # row만 네트워크에 속해있는 경우
                    # col만 네트워크에 속해있는 경우
                    networkNum = max(node[row], node[col])
                    node[row] = networkNum
                    node[col] = networkNum
                else :
                    # row, col 둘 다 네트워크에 속해있지 않는 경우
                    answer += 1
                    node[row] = answer
                    node[col] = answer
    
    return computers

def solution(n, computers):
    answer = 0

    visited = [False for _ in range(n)]

    for row in range(n):
        if visited[row] == False:
            dfs(n, computers, visited, row)
            answer += 1
    return answer

def dfs(n, computers, visited, row):
    visited[row] = True
    for col in range(n):
        if row != col and computers[row][col] == 1 and visited[col] == False:
                dfs(n, computers, visited, col)

def solution2(n, computers):
    answer = 0
    
    visited = [False for _ in range(n)]
    
    for row in range(n):
        if visited[row] == False:
            bfs(n, computers, visited, row)
            answer += 1
    return answer
def bfs(n, computers, visited, row):
    visited[row] = True
    que = []
    que.append(row)
    
    while que:
        row = que.pop(0)
        visited[row] = True
        
        for col in range(n):
            if row != col and computers[row][col] == 1 and visited[col] == False:
                bfs(n,computers, visited, col)