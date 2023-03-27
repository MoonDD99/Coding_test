from collections import deque,defaultdict
def getAdjustBlockNum(floor, adjust):
    result = []
    adjustStack = deque(adjust)
    for block in floor:
        adjust = 1
        while adjustStack and adjustStack[0] <= block:
            if adjustStack[0] < block:
                adjust += 1
            adjustStack.popleft()
        result.append(adjust)
    return result

def Solution(walls):
    adjustLocation = defaultdict(list) #인접한블럭갯수 : [해당 블럭들 위치]
    
    #누적합 구하기
    wallsSum = []
    for row in range(len(walls)):
        floorSum = []
        total = 0
        for col in range(len(walls[row])):
            total += walls[row][col]
            floorSum.append(total)
        wallsSum.append(floorSum)

    #인접한 블럭들 개수들 구하기
    for row in range(len(walls)):
        if row == 0:
            adjustBlock = getAdjustBlockNum(wallsSum[row], wallsSum[row+1])

            for col in range(len(walls[row])):
                adjustNum = 2
                if col == 0 or col == (len(walls[row])-1):
                    adjustNum = 1 + adjustBlock[col]
                    print(adjustNum)
                else:
                    adjustNum += adjustBlock[col]
                adjustLocation[adjustNum].append((row,col))
        elif row == (len(walls)-1):
            adjustBlock = getAdjustBlockNum(wallsSum[row], wallsSum[row-1])
            for col in range(len(walls[row])):
                adjustNum = 2
                if col == 0 or col == (len(walls[row])-1):
                    adjustNum = 1 + adjustBlock[col]
                else:
                    adjustNum += adjustBlock[col]
                adjustLocation[adjustNum].append((row,col))
        else :
            adjustBlockUp = getAdjustBlockNum(wallsSum[row],wallsSum[row+1])
            adjustBlockDown = getAdjustBlockNum(wallsSum[row], wallsSum[row-1])

            for col in range(len(walls[row])):
                adjustNum = 2
                if col == 0 or col == (len(walls[row])-1):
                    adjustNum = 1 + adjustBlockUp[col] + adjustBlockDown[col]
                else:
                    adjustNum += (adjustBlockUp[col] + adjustBlockDown[col])
                    print(adjustBlockUp[col] + adjustBlockDown[col])
                adjustLocation[adjustNum].append((row,col))
        
    print(adjustLocation)


walls = [[3,1,1,2],[2,3,2],[1,1,2,3]]
Solution(walls)