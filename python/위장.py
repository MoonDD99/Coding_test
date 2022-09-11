from collections import Counter
from functools import reduce

def solution(clothes):
    clothDict = {}

    for cloth, type in clothes:
        clothDict[type] = clothDict.get(type,0) + 1

    clothDict = Counter(type for name , type in clothes)

    answer = reduce(lambda x, y : x * (y + 1), clothDict.values(), 1) - 1

    return answer

#clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
answer = solution(clothes)
print(answer)