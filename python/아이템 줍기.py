from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] 

    graph = makeGraph(rectangle)

    que = deque()
    que.append((characterY*2, characterX*2))

    while que:
        y,x = que.popleft()
        #print("x : " + str(x) + " y : " +  str(y) + " distance : " + str(graph[y][x]))
        if x == 2 * itemX and y == 2 * itemY:
            return graph[y][x] // 2

        for index in range(4):
            nextX = x + dx[index]
            nextY = y + dy[index]

            if graph[nextY][nextX] == 1: 
                que.append((nextY,nextX))
                graph[nextY][nextX] = graph[y][x] + 1
            


    return answer

def makeGraph(rectangles):
    graph = [[-1] * 102 for _ in range(102)] # 빈곳 : -1 직사각형 내부 : 0 테두리 : 1

    for rectangle in rectangles:
        lx, ly, rx, ry = map(lambda x : x*2,rectangle) #[좌x, 좌y, 우x, 우y]
        for row in range(ly, ry+1, 1):
            for col in range(lx, rx+1, 1):
                if lx < col < rx and ly < row < ry:
                    #테두리 : 1
                    graph[row][col] = 0
                elif graph[row][col] != 0:
                    #직사각형 내부 : 0
                    graph[row][col] = 1
    return graph

def checkGraph(rectangle):
    newGraph = makeGraph(rectangle)
    for row in range(51):
        for col in range(51):
            if newGraph[row][col] == 1:
                print((row,col))

rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
characterX = 9
characterY = 7	
itemX = 6
itemY = 1
#checkGraph(rectangle)
answer = solution(rectangle, characterX, characterY, itemX, itemY)
print(answer)
