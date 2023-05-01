from collections import deque
import sys

location = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),0:(3,1)}

def distance(startNum, targetNum): 
    start = location[startNum]
    target = location[targetNum]
    
    weight = 0
    if start == target :
        return 1

    diffRow = abs(start[0]-target[0])
    diffCol = abs(start[1]-target[1])

    if diffRow >= 1 and diffCol >= 1:
        if diffRow <= diffCol:
            return diffRow * 3 + (diffCol-diffRow) * 2
        return diffCol * 3 + (diffRow-diffCol) * 2
    else:
        return diffRow * 2 + diffCol * 2
    
def solution(numbers):
    distances = set()
    minResult = 1000000
    
    stack = deque([[0,4,6,0]]) #[depth, left, right, weight]
    
    while stack:
        depth, left, right, weight = stack.pop()
        number = int(numbers[depth])
        
        if depth == len(numbers)-1:
            leftDistance = weight + distance(left,number)
            rightDistance = weight + distance(right,number)
            
            minResult = min([minResult, leftDistance, rightDistance])
    
        else:
            leftElement = [depth+1, number, right, weight+distance(left, number)]
            rightElement = [depth+1, left, number, weight+distance(right, number)]
            
            stack.append(leftElement)
            stack.append(rightElement)
            
    return minResult
    
        

    
    
    