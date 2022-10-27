def failSolution(number, k):
    result = ""
    restLen = len(number) - k
    maxIndex = 0
    for _ in range(0,restLen) :
        for index in range(maxIndex + 1, len(number) - restLen + 1):
            if number[maxIndex] < number[index]:
                maxIndex = index    
        result += number[maxIndex]
        restLen -= 1
        maxIndex += 1

    return result            
def solution(number, k):
    result = []
    
    for num in number:
        while result and result[-1] < num and k > 0 :
            result.pop()
            k -= 1
        result.append(num)
    
    print(result)
    return ''.join(result[:len(result) - k])
number = "1924"
k = 2
result = solution(number, k)
number = "1231234"
k = 3
result = solution(number, k)
number ="4177252841"
k = 4 
number = "987654"
k = 2
result = solution(number, k)
print(result)