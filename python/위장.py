from collections import Counter
from functools import reduce
from collections import defaultdict

def solution(clothes):
    clothDict = Counter(type for name , type in clothes)

    answer = reduce(lambda x, y : x * (y + 1), clothDict.values(), 1) - 1

    return answer


def solution1(clothes):
    answer = 1
    clothDict = defaultdict(list)
    for cloth, kind in clothes:
        clothDict[kind].append(cloth)
    for cloth, kind in clothDict.items():
        answer *= (len(kind) + 1)
        
    return answer - 1

#clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
answer = solution(clothes)
print(answer)
