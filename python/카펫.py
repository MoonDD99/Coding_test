def solution(brown, yellow):
    returnDict = {}
    total = brown + yellow

    for index in range(2, int(total**0.5)+1):
        div, mod = divmod(total, index)
        if mod == 0:
            if (index-2)*(div-2) == yellow:
                returnDict[div - index] = [div, index]
    answer = min(returnDict.keys())
    return returnDict[answer]

brown, yellow = 10,2
brown, yellow = 8,1
brown, yellow = 24,24
brown, yellow = 18,6
answer = solution(brown, yellow)
print(answer)
