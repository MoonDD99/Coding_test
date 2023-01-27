def solution(word):
    charNum = {'A':1, 'E':2, 'I':3, 'O':4, 'U':5}
    result = 0
    for i in range(1,len(word)+1):
        k = 0
        for j in range(1,(6-i)):
            k += 5**j
        result += (charNum[word[i-1]]-1) * k + charNum[word[i-1]]
    return result

def solution1(word):
    answer = 0
    alphaNum = {'A':1, 'E':2, 'I':3, 'O':4, 'U': 5}
    for wordIndex in range(len(word)):
        k = 0
        for square in range(1,5-wordIndex):
            k += 5**square
        answer += k * (alphaNum[word[wordIndex]] - 1) + alphaNum[word[wordIndex]]
    return answer

word = "EIO" #"I" #"AAAAE" #"AAAE" 
result = solution(word)
print(result)

# 'A':1, 'E':2, 'I':3, 'O':4, 'U':5
# (문자번호 - 1) * (5**4+5**3+5**2+5**1) + 문자번호 + (문자번호 - 1) * (5**3+5**2+5**1) + 문자번호 + (문자번호 - 1) * (5**2+5**1) + 문자번호 + (문자번호 - 1) * (5**1) + 문자번호