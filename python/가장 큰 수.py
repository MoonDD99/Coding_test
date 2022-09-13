def solution(numbers):
    answer = ''
    stringNumbers = []

    for number in numbers:
        stringNumbers.append(str(number))
    
    #stringNumbers.sort(reverse=True)
    sortStringNumbers = sorted(stringNumbers, key=lambda x:x*4, reverse=True)
    #sortNumbers = sorted(list(map(str, numbers)), key=lambda x: x*5, reverse=True)
    for stringNumber in sortStringNumbers:
        answer += stringNumber

    return str(int(answer))

#numbers = [6, 10, 2]
#numbers = [3, 30, 34, 5, 9]
numbers = [0,0,0,0]
answer = solution(numbers)
print(answer)