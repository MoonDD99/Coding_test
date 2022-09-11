def solution(clothes):
    clothDict = {}

    for cloth, type in clothes:
        clothDict[type] = clothDict.get(type,0) + 1

    print(clothDict)
    
    answer = 1
    for clothType in clothDict:
        answer *= (clothDict[clothType] + 1)

    
    return answer - 1

#clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
answer = solution(clothes)
print(answer)