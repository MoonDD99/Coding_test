from collections import deque
def solution(maps):
    visited = list()
    que = deque()
    que.append((0,0))
    answerList = []
    answer = 0
    
    while que:
        location = que.pop()
        row = location[0]
        col = location[1]
        if location not in visited:
            answer += 1
        
            if row == (len(maps)-1) and col == (len(maps[0]) -1):
                answerList.append(answer)
            if maps[row][col] == 1 and location not in visited:
                visited.append(location)
                if row != 0 and maps[row-1][col] == 1:
                    que.append((row-1,col))
                if col != 0 and maps[row][col-1] == 1:
                    que.append((row,col-1))
                if row+1 < len(maps) and maps[row+1][col] == 1:
                    que.append((row+1,col))
                if col+1 < len(maps[0]) and maps[row][col+1] == 1:
                    que.append((row,col+1))
    
    if len(answerList) == 0:
        return -1
    return min(answerList)
 
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	
answer = solution(maps)
print(answer)




