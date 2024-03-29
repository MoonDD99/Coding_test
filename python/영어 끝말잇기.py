import math
def solution(n, words):
    #score : 100.0 / 100.0
    answer = [0,0]
    last_char = (words[0])[len(words[0])-1]
    exist_word = [words[0]]
    
    for index in range(1,len(words)):
        word = words[index]
        if last_char != word[0] or word in exist_word :
            answer[0] = index % n + 1
            answer[1] = math.ceil((index+1)/n)
            break
        else :
            last_char = word[len(word)-1]
            exist_word.append(word)

    return answer

from math import ceil
def solution1(n, words):
    answer = []
    visited = {}
    lenWords = len(words)
    
    lastChar = (words[0])[0]
    
    for index in range(lenWords):
        word = words[index]
        if lastChar != word[0] or word in visited or len(word) == 1:
            return [(index % n)+1, ceil((index+1)/n)]
        else:
            visited[word] = 0
            lastChar = word[-1]

    return [0,0]