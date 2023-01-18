from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] 

    graph = makeGraph(rectangle)

    que = deque()
    que.append((characterY, characterX))

    while que:
        y,x = que.popleft()
        print("x : " + str(x) + " y : " +  str(y) + " distance : " + str(graph[y][x]))
        if x == itemX and y == itemY:
            return graph[y][x] - 1

        for index in range(4):
            nextX = x + dx[index]
            nextY = y + dy[index]

            if nextX >= 0 and nextX <= 50 and nextY >=0 and nextY <= 50 and graph[nextY][nextX] == 1:
                que.append((nextY,nextX))
                graph[nextY][nextX] = graph[y][x] + 1
            


    return answer

def makeGraph(rectangles):
    graph = [[-1] * 51 for _ in range(51)] # 빈곳 : -1 직사각형 내부 : 0 테두리 : 1

    for rectangle in rectangles:
        lx, ly, rx, ry = rectangle #[좌x, 좌y, 우x, 우y]
        for row in range(ly, ry+1, 1):
            for col in range(lx, rx+1, 1):
                if (graph[row][col] != 0) and ((row == ly and col <= rx) or (row == ry and col <= rx) or (row <= ry and col == lx) or (row <= ry and col == rx)): #not내부 and (밑변 or 윗변 or 좌변 or 우변)
                    #테두리 : 1
                    graph[row][col] = 1
                else:
                    #직사각형 내부 : 0
                    graph[row][col] = 0
    return graph

def checkGraph(rectangle):
    newGraph = makeGraph(rectangle)
    for row in range(51):
        for col in range(51):
            if newGraph[row][col] == 1:
                print((row,col))

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY = 3	
itemX = 7
itemY = 8
#checkGraph(rectangle)
answer = solution(rectangle, characterX, characterY, itemX, itemY)
#print(answer)
