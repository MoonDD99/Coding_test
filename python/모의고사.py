answerNumDict = {1:0,2:0,3:0}
answerDict = {1:"12345", 2:"21232425",3:"3311224455"}
def solution(answers):
    answer = set()
    lenOfAnswers = len(answers)

    #answers 길이만큼 수포자들의 answer길이 늘리기
    first = divmod(lenOfAnswers,5)
    answerDict[1] = answerDict[1] * first[0] + (answerDict[1])[:first[1]]
    second = divmod(lenOfAnswers,8)
    answerDict[2] = answerDict[2] * second[0] + (answerDict[2])[:second[1]]
    third = divmod(lenOfAnswers,10)
    answerDict[3] = answerDict[3] * third[0] + (answerDict[3])[:third[1]]

    #정답맞추기
    for index in range(1,4,1):
        for answerIndex in range(0,lenOfAnswers):
            if int((answerDict[index])[answerIndex]) == answers[answerIndex]:
                answerNumDict[index] += 1

    print(answerNumDict)
    for index in range(1,3,1):
        if answerNumDict[index] >= answerNumDict[index+1]:
            if answerNumDict[index] == answerNumDict[index+1]:
                answer.update([index])
                answer.update([index+1])
            else :
                answer = {index}
        else :
            answer.update([index])
    
    return list(answer)

answers = [1,2,3,4,5]
#answers = [1,3,2,4,2]
result = solution(answers)
print(result)