from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    que = deque()
    que.append([begin,0])

    while que:
        begin, depth = que.popleft()

        if begin == target:
            return depth

        for index in range(len(words)):
            if canChange(begin, words[index]):
                que.append([words[index], depth+1])
    
    return 0


def canChange(previous, next):
    count = 0
    
    for index in range(len(previous)):
        if previous[index] != next[index]:
            count += 1

    return True if count == 1 else False
    
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
answer = solution(begin, target, words)
print(answer)