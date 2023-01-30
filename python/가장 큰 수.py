def solution(numbers):
    answer = ''
    stringNumbers = []

    for number in numbers:
        stringNumbers.append(str(number))

    sortStringNumbers = sorted(stringNumbers, key=lambda x:x*3, reverse=True)

    for stringNumber in sortStringNumbers:
        answer += stringNumber

    return str(int(answer))

def failSolution(numbers):
    answer = ''
    stringNumbers = []

    for number in numbers:
        stringNumbers.append(str(number))

    sortStringNumbers = sorted(stringNumbers, key=lambda x:x*3, reverse=True)

    for stringNumber in sortStringNumbers:
        answer += str(int(stringNumber)) #여기서 int로 바꾸면 [0,0,0,0]에서 answer에서 "0000"으로 출력된다

    return answer 

numbers = [6, 10, 2]
#numbers = [3, 30, 34, 5, 9]
#numbers = [0,0,0,0]
answer = solution(numbers)
print(answer)