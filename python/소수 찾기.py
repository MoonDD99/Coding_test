from itertools import permutations

def isPrimeNum(number):
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5)+1):
        if number % divisor == 0:	
            return False
    return True

def solution(numbers):
    primeNumSet = set()
    numbersArray = list(numbers)

    #가능한 모든 숫자 만들기 string-> int
    for i in range(1,len(numbers)+1,1):
        possiblePermutations = list(permutations(numbersArray,i))
        for permutation in possiblePermutations:
            number = int(''.join(permutation))
            #소수인지 검사
            if isPrimeNum(number):
                #numberSet에 저장
                primeNumSet.add(number)
    
    #primeNumSet 길이 return
    print(primeNumSet)
    return len(primeNumSet)

#numbers = "17"
#numbers = "011"
numbers = "1231"
print(isPrimeNum(1))
answer = solution(numbers)
print(answer)