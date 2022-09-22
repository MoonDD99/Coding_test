import itertools

def solution(k, dungeons):
    maxNum = 0
    totalCases = itertools.permutations(dungeons, len(dungeons))

    for case in totalCases:
        visit = 0
        currentTired = k
        for minRequired, consumed in case:
            if currentTired >= minRequired:
                currentTired -= consumed
                visit += 1
        maxNum = max(maxNum, visit)
    return maxNum

k = 80
dungeons = [[80,20],[50,40],[30,10]]
answer = solution(k, dungeons)
print(answer)