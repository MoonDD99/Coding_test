"""

input = value : [int, int] -> [미세먼지농도, 초미세먼지농도]
output = result : (bool, bool) -> (마스크여부, 마스크재사용여부)

"""
def isMask (value):
    mask = False
    reuse = False
    if value[0] >= 151:
        mask = True
        if value[1] >= 76:
            reuse = True
        return (mask, reuse)
    elif value[0] >= 81:
        mask = True
        return (mask, reuse)
    else :
        if value[1] >= 36:
            mask = True
            return (mask, reuse)
    return (mask, reuse)

def solution(atmos):
    answer = 0
    index = 0
    while index < len(atmos):
        result = isMask(atmos[index])
        if result[0]:
            answer += 1
            if result[1] == False:
                index += 2
        index += 1
    return answer

input = [[30, 15], [80, 35]]
result = solution(input)
print(result)

