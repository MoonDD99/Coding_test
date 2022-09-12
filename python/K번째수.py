def solution(array, commands):
    answer = []

    for command in commands:
        firstIndex = command[0] - 1
        lastIndex = command[1] - 1
        kIndex = command[2] - 1

        cutArray = array[firstIndex : lastIndex + 1]
        cutArray.sort()

        answer.append(cutArray[kIndex])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = solution(array, commands)
print(answer)