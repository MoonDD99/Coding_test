## 자료구조
# 딕셔너리 -> 캐릭터 : 점수

personalType =  {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
# 배열 -> ["RT", "CF", "JM", "AN"]
personalPointer = ["RT", "CF", "JM", "AN"]

# 함수
## Survey에서 지표의 캐릭터 별 점수 계산
def calculateType(surveys, choices):
    for index in range(len(surveys)) :
        choice = choices[index]
        survey = surveys[index]

        if choice < 4 : 
            personalType[survey[0]] += choice
        else :
            personalType[survey[1]] += (choice - 4)

## 주어진 지표 점수 계산해서 캐릭터 반환
def calculatePointer(pointer) :
    if personalType[pointer[0]] >= personalType[pointer[1]] :
        if personalType[pointer[0]] == personalType[pointer[1]] :
            return pointer[0]
        return pointer[0]
    return pointer[1]

def solution(survey, choices):
    answer = ''
    
    calculateType(survey,choices)
    
    # 코드
    ## 지표담긴 배열의 모든 원소들 캐릭터 반환하여 최종 return
    for pointer in personalPointer:
        answer += calculatePointer(pointer)

    return answer


survey = ["TR", "RT", "TR"]
choices = 	[7, 1, 3]
result = solution(survey, choices)
print(result)