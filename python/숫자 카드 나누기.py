import math
def solution(arrayA, arrayB):
    answer = 0
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    
    for index in range(1,len(arrayA)):
        gcdA = math.gcd(gcdA, arrayA[index])
        gcdB = math.gcd(gcdB, arrayB[index])
    
    for num in arrayA:
        if num % gcdB == 0:
            gcdB = 1
            break
    
    for num in arrayB:
        if num % gcdA == 0:
            gcdA = 1
            break
            
    if gcdA == 1 and gcdB == 1:
        return 0
    elif gcdA != 1 or gcdB != 1:
        return max(gcdA, gcdB)
